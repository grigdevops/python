#!/bin/bash
docker-compose -f /script/streamer/docker-compose.yml -f /script/streamer/docker-compose.prod.yml down
docker-compose -f /script/streamer/docker-compose.yml -f /script/streamer/docker-compose.prod.yml up --build