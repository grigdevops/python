#!/bin/bash
docker-compose -f /home/armen/streamer/docker-compose.yml -f /home/armen/streamer/docker-compose.prod.yml down
docker-compose -f /home/armen/streamer/docker-compose.yml -f /home/armen/streamer/docker-compose.prod.yml up --build