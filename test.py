    def create_cloudfront(self, cloudfront_cfg):
        cloudfront_name = cloudfront_cfg.get("name")
        s3_bucket_name = cloudfront_cfg["origin_cfg"].get("s3_bucket_name")
        aliases = cloudfront_cfg.get("aliases")

        cloudfront_obj = cloudfront.Distribution(
            self, id=self.create_logical_id(f'{cloudfront_name}-distribution'),
            default_behavior=cloudfront.BehaviorOptions(
                allowed_methods=getattr(cloudfront.AllowedMethods,
                                        cloudfront_cfg.get("allowed_methods", "ALLOW_GET_HEAD")),
                viewer_protocol_policy=getattr(cloudfront.ViewerProtocolPolicy,
                                               cloudfront_cfg.get("viewer_protocol", "REDIRECT_TO_HTTPS")),
                cached_methods=getattr(cloudfront.CachedMethods,
                                       cloudfront_cfg.get("cached_methods", "CACHE_GET_HEAD")),
                compress=cloudfront_cfg.get("compress", False),
                smooth_streaming=cloudfront_cfg.get("smooth_streaming", False),
                cache_policy=self.create_cache_policy(cloudfront_cfg=cloudfront_cfg, cloudfront_name=cloudfront_name),
                origin=self.create_origin(
                    origin_type=cloudfront_cfg.get("origin_type", "S3Origin"),
                    cloudfront_name=cloudfront_name,
                    origin_cfg=cloudfront_cfg.get("origin_cfg", {}),
                    s3_bucket_name=s3_bucket_name
                ),
                edge_lambdas=self.edge_lambda_list(functions=cloudfront_cfg.get("functions")),
            ),
            error_responses=self.error_responses_list(error_responses=cloudfront_cfg.get("error_responses")),
            price_class=getattr(cloudfront.PriceClass, cloudfront_cfg.get("price_class", "PRICE_CLASS_ALL")),
            enabled=cloudfront_cfg.get("enabled", True),
            certificate=acm.Certificate.from_certificate_arn(
                self, id=self.create_logical_id(f'{cloudfront_name}-acm'),
                certificate_arn=cloudfront_cfg["certificate"]),
            domain_names=self.domain_names_list(
                aliases=aliases, hz_name=cloudfront_cfg.get("hz").get("hz_name")),
            enable_logging=cloudfront_cfg.get("enable_logging"),
            log_bucket=cloudfront_cfg.get("log_bucket"),
            log_file_prefix=cloudfront_cfg.get("log_file_prefix"),
            log_includes_cookies=cloudfront_cfg.get("log_includes_cookies"),
            comment=cloudfront_cfg.get("comment"),
            http_version=getattr(cloudfront.HttpVersion, cloudfront_cfg.get("http_version", "HTTP2")),
            enable_ipv6=cloudfront_cfg.get("enable_ipv6", True),
            web_acl_id=cloudfront_cfg.get("web_acl_id"),
            default_root_object=cloudfront_cfg.get("default_root_object"),
        )

        self.set_ssm_string_parameter(f'{cloudfront_name}', cloudfront_obj.distribution_id)

        if aliases:
            alias_target = r53target.CloudFrontTarget(cloudfront_obj)
            self.create_dns_record(
                aliases=aliases, alias_target=alias_target, hz_cfg=cloudfront_cfg.get("hz"))

        return cloudfront_obj

    def create_dns_record(self, aliases, alias_target, hz_cfg):
        for record in aliases:
            record = self.get_hash_string(record, 63)
            record_props = {
                "zone": r53.HostedZone.from_hosted_zone_attributes(
                    self, id=self.create_logical_id(f'{hz_cfg.get("hz_name")}-hz-{record}'),
                    hosted_zone_id=hz_cfg.get("hz_id"),
                    zone_name=hz_cfg.get("hz_name")
                ),
                "target": r53.RecordTarget.from_alias(alias_target=alias_target),
            }

            if record != "zone_root":
                record_props["record_name"] = record

            r53.ARecord(
                self, f'{hz_cfg.get("hz_name")}-{record}',
                **record_props
            )

    def domain_names_list(self, hz_name, aliases=None):
        domain_names = None
        if aliases:
            domain_names = []
            for alias in aliases:
                alias = self.get_hash_string(alias, 63)
                domain_name = f'{alias}.{hz_name}'
                if alias == "zone_root":
                    domain_name = hz_name
                domain_names.append(domain_name)

        return domain_names

    def edge_lambda_list(self, functions=None):
        edge_lambdas = None
        if functions:
            edge_lambdas = []
            for function in functions:
                edge_lambda = cloudfront.EdgeLambda(
                    event_type=getattr(cloudfront.LambdaEdgeEventType, function.get("event_type")),
                    function_version=lb.Version.from_version_arn(
                        self,
                        id=self.create_logical_id(f'{function.get("name")}-{function.get("event_type")}-function'),
                        version_arn=self.get_ssm_string(f'lambda/{function.get("name")}-version-arn')
                    )
                )
                edge_lambdas.append(edge_lambda)
        return edge_lambdas

    @staticmethod
    def error_responses_list(error_responses=None):
        error_responses_objects_list = None
        if error_responses:
            error_responses_objects_list = []
            for error_response in error_responses:
                error_responses_object = cloudfront.ErrorResponse(
                    http_status=int(error_response.get('http_status')),
                    response_http_status=int(error_response.get('response_http_status')),
                    response_page_path=error_response.get('response_page_path'),
                    ttl=Duration.seconds(int(error_response.get('ttl'))),
                )
                error_responses_objects_list.append(error_responses_object)
        return error_responses_objects_list

    def create_origin(self, origin_type, origin_cfg, cloudfront_name, s3_bucket_name=None):
        origin_obj = None
        if origin_type == "S3Origin":
            bucket = self.get_s3_bucket(
                bucket_name=s3_bucket_name, region=origin_cfg.get("s3_bucket_region", "eu-central-1"),
                cloudfront_name=cloudfront_name)

            origin_access_identity = self.get_origin_access_identity(cloudfront_name, bucket_name=bucket.bucket_name)

            origin_obj = origin.S3Origin(
                bucket=bucket,
                origin_access_identity=origin_access_identity,
                origin_path=origin_cfg.get("origin_path"),
                connection_attempts=origin_cfg.get("connection_attempts", 3),
                connection_timeout=Duration.seconds(origin_cfg.get("connection_timeout", 10)),
            )
        elif origin_type == "HttpOrigin":
            origin_obj = origin.HttpOrigin(
                domain_name=origin_cfg.get("domain_name"),
                connection_attempts=origin_cfg.get("connection_attempts"),
                connection_timeout=Duration.seconds(origin_cfg.get("connection_timeout")),
                protocol_policy=getattr(cloudfront.OriginProtocolPolicy, origin_cfg.get("protocol_policy")),
                http_port=origin_cfg.get("http_port"),
                https_port=origin_cfg.get("https_port"),
                keepalive_timeout=Duration.seconds(origin_cfg.get("keepalive_timeout")),
                read_timeout=Duration.seconds(origin_cfg.get("read_timeout")),
            )
        return origin_obj

    def get_s3_bucket(self, bucket_name, region, cloudfront_name):
        bucket = s3.Bucket.from_bucket_attributes(
            self, id=self.create_logical_id(f'{cloudfront_name}-bucket'),
            bucket_name=bucket_name,
            region=region
        )
        return bucket

    def get_origin_access_identity(self, cloudfront_name, bucket_name):
        origin_access_identity = cloudfront.OriginAccessIdentity.from_origin_access_identity_id(
            self, id=self.create_logical_id(f'{cloudfront_name}-origin-access-identity'),
            origin_access_identity_id=self.get_ssm_string(f's3/{bucket_name}-oai')
        )
        return origin_access_identity

    def create_cache_policy(self, cloudfront_cfg, cloudfront_name):
        if "cache_policy_id" in cloudfront_cfg:
            cache_policy = cloudfront.CachePolicy.from_cache_policy_id(
                self, id=self.create_logical_id(f'{cloudfront_name}-cache-policy'),
                cache_policy_id=cloudfront_cfg.get("cache_policy_id")
            )
        elif "cache_policy_cfg" in cloudfront_cfg:
            cache_policy_cfg = cloudfront_cfg.get("cache_policy_cfg")
            params = {}
            for behavior in cache_policy_cfg.get("behaviors"):
                behavior_class = getattr(cloudfront, behavior.get("class"))
                if behavior.get("behavior_type") == "none":
                    params[behavior.get("type")] = behavior_class.none()
                elif behavior.get("behavior_type") == "all":
                    params[behavior.get("type")] = behavior_class.all()
                elif behavior.get("behavior_type") == "allow_list":
                    params[behavior.get("type")] = behavior_class.allow_list(*behavior.get("list"))
                elif behavior.get("behavior_type") == "deny_list":
                    params[behavior.get("type")] = behavior_class.deny_list(*behavior.get("list"))

            cache_policy_obj = cloudfront.CachePolicy(
                self, id=self.create_logical_id(f'{cache_policy_cfg["name"]}-cache-policy'),
                cache_policy_name=cache_policy_cfg.get("name"),
                comment=cache_policy_cfg.get("comment"),
                default_ttl=Duration.seconds(cache_policy_cfg["default_ttl"]),
                min_ttl=Duration.seconds(cache_policy_cfg["min_ttl"]),
                max_ttl=Duration.seconds(cache_policy_cfg["max_ttl"]),
                enable_accept_encoding_gzip=cache_policy_cfg.get("enable_accept_encoding_gzip"),
                enable_accept_encoding_brotli=cache_policy_cfg.get("enable_accept_encoding_brotli"),
                **params
            )
            cache_policy = cache_policy_obj
        else:
            cache_policy = getattr(cloudfront.CachePolicy, cloudfront_cfg.get("cache_policy", "CACHING_OPTIMIZED"))

        return cache_policy

    @staticmethod
    def get_hash_string(name, max_len):
        string_length = max_len - 9
        if len(name) > max_len:
            hash_str = hashlib.md5(name.encode('utf-8')).hexdigest()[:7]
            name = f"{name[:string_length]}-{hash_str}"
        return name




###############################################################
def create_cloudfront(self, cloudfront_cfg, s3_stack):

        cache_policy = ''
        error_responses_objects_list = None
        if "cache_policy_id" in cloudfront_cfg:
            cache_policy = cloudfront_cfg["cache_policy_id"],
        elif "cache_policy_cfg" in cloudfront_cfg:
            cache_policy_cfg = cloudfront_cfg["cache_policy_cfg"]
            params = {}
            for behavior in cache_policy_cfg["behaviors"]:
                behavior_class = getattr(cloudfront, behavior["class"])
                if behavior["behavior_type"] == "none":
                    params[behavior["type"]] = behavior_class.none()
                elif behavior["behavior_type"] == "all":
                    params[behavior["type"]] = behavior_class.all()
                elif behavior["behavior_type"] == "allow_list":
                    params[behavior["type"]] = behavior_class.allow_list(*behavior["list"])
                elif behavior["behavior_type"] == "deny_list":
                    params[behavior["type"]] = behavior_class.allow_list(*behavior["list"])

            cache_policy_obj = cloudfront.CachePolicy(
                self, id=self.create_logical_id(f'{cache_policy_cfg["name"]}-cache-policy'),
                cache_policy_name=cache_policy_cfg["name"],
                comment=cache_policy_cfg["comment"],
                default_ttl=Duration.seconds(cache_policy_cfg["default_ttl"]),
                min_ttl=Duration.seconds(cache_policy_cfg["min_ttl"]),
                max_ttl=Duration.seconds(cache_policy_cfg["max_ttl"]),
                enable_accept_encoding_gzip=cache_policy_cfg["enable_accept_encoding_gzip"],
                enable_accept_encoding_brotli=cache_policy_cfg["enable_accept_encoding_brotli"],
                **params
            )
            cache_policy = cache_policy_obj
        elif "cache_policy" in cloudfront_cfg:
            cache_policy = getattr(cloudfront.CachePolicy, cloudfront_cfg["cache_policy"])

        params = {}
        if "enable_logging" in cloudfront_cfg:
            params["enable_logging"] = cloudfront_cfg["enable_logging"]
            params["log_bucket"] = cloudfront_cfg["log_bucket"]
            params["log_file_prefix"] = cloudfront_cfg["log_file_prefix"]
            params["log_includes_cookies"] = cloudfront_cfg["log_includes_cookies"]

        if 'error_responses' in cloudfront_cfg:
            error_responses_objects_list = []
            for error_response in cloudfront_cfg['error_responses']:
                error_responses_object = cloudfront.ErrorResponse(
                    http_status=int(error_response['http_status']),
                    response_http_status=int(error_response['response_http_status']),
                    response_page_path=error_response['response_page_path'],
                    ttl=Duration.seconds(int(error_response['ttl'])),
                )
                error_responses_objects_list.append(error_responses_object)

        bucket = getattr(s3_stack, cloudfront_cfg["s3_bucket_name"])

        origin_obj = origin.S3Origin(
            bucket=bucket,
            origin_path=cloudfront_cfg['origin_path']
        )

        domain_names = []
        for alias in cloudfront_cfg['aliases']:
            domain_name = f'{alias}.{cloudfront_cfg["hz_name"]}'
            domain_names.append(domain_name)

        cloudfront_obj = cloudfront.Distribution(
            self, id=self.create_logical_id(f'{cloudfront_cfg["name"]}-distribution'),
            default_behavior=cloudfront.BehaviorOptions(
                allowed_methods=getattr(cloudfront.AllowedMethods, cloudfront_cfg["allowed_methods"]),
                viewer_protocol_policy=getattr(cloudfront.ViewerProtocolPolicy, cloudfront_cfg["viewer_protocol"]),
                cached_methods=getattr(cloudfront.CachedMethods, cloudfront_cfg["cached_methods"]),
                compress=cloudfront_cfg["compress"],
                smooth_streaming=cloudfront_cfg["smooth_streaming"],
                cache_policy=cache_policy,
                origin=origin_obj
            ),
            error_responses=error_responses_objects_list,
            price_class=getattr(cloudfront.PriceClass, cloudfront_cfg["price_class"]),
            enabled=cloudfront_cfg["enabled"],
            certificate=acm.Certificate.from_certificate_arn(
                self, id=self.create_logical_id(f'{cloudfront_cfg["name"]}-acm'),
                certificate_arn=cloudfront_cfg["certificate"]),
            domain_names=domain_names,
            **params
        )

        # s3_origin_source = cloudfront.S3OriginConfig(s3_bucket_source=origin_obj)
        #
        # source_config = cloudfront.SourceConfiguration(
        #     s3_origin_source=s3_origin_source,
        #     origin_path=cloudfront_cfg['origin_path'],
        #     behaviors=[cloudfront.Behavior(is_default_behavior=True)]
        # )
        #
        # cloudfront_obj = cloudfront.CloudFrontWebDistribution(
        #     self, id=self.create_logical_id(f'{cloudfront_cfg["name"]}-distribution'),
        #     origin_configs=[source_config]
        # )

        r53_cloudfront_target = r53target.CloudFrontTarget(cloudfront_obj)

        for record in cloudfront_cfg['aliases']:
            r53.ARecord(self, f'{cloudfront_cfg["name"]}-{record}',
                        zone=r53.HostedZone.from_hosted_zone_attributes(
                            self, id=self.create_logical_id(f'{cloudfront_cfg["name"]}-hz-{record}'),
                            hosted_zone_id=cloudfront_cfg["hz_id"],
                            zone_name=cloudfront_cfg["hz_name"]
                        ),
                        target=r53.RecordTarget.from_alias(alias_target=r53_cloudfront_target),
                        record_name=record,
                        )

        return cloudfront_obj
