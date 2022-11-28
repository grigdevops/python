'#!/bin/bash
CONTAINER_NAME=streamer-inorain-streamer-1

IS_RUNING=$(docker ps | grep $CONTAINER_NAME)
if [ ${#IS_RUNING} -ge 1 ];
   then echo "RUNNING NOW"; exit
        else
        docker-compose -f full_path_to_project/docker-compose.yml -f full_path_to_project/docker-compose.prod.yml up -d
fi
