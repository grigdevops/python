#!/bin/bash
CONTAINER_NAME=streamer-inorain-streamer-1

IS_RUNING=$(docker ps | grep $CONTAINER_NAME)
if [ ${#IS_RUNING} -ge 1 ];
   then echo "RUNNING NOW"; exit
        else
        docker-compose -f {project_path}/docker-compose.yml -f {project_path}/docker-compose.prod.yml up -d
fi