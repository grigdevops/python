import os


# sys module for path arguments  day_streamer
import sys
project_path = sys.argv[1]
# execution time run
os.system(f"cd {project_path}/streamer && docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d")
os.system("sudo apt-get install -y net-tools htop nano")


# TODO check file exist delete, new files
isFileHealth = os.path.isfile("healthcheck.sh")
if isFileHealth:
    os.remove("healthcheck.sh")
isFileRestart = os.path.isfile("day_restart.sh")
if isFileRestart:
    os.remove("day_restart.sh")

os.system("touch healthcheck.sh && touch day_restart.sh")
os.system("chmod +x healthcheck.sh")
os.system("chmod +x day_restart.sh")
print(f"{isFileHealth} is exist")
print(f"{isFileRestart} is exist")



dayrestart_str = f'''#!/bin/bash
docker-compose -f {project_path}/streamer/docker-compose.yml -f {project_path}/streamer/docker-compose.prod.yml down
docker-compose -f {project_path}/streamer/docker-compose.yml -f {project_path}/streamer/docker-compose.prod.yml up --build'''

healthcheck_str = ''''#!/bin/bash
CONTAINER_NAME=streamer-inorain-streamer-1

IS_RUNING=$(docker ps | grep $CONTAINER_NAME)
if [ ${#IS_RUNING} -ge 1 ];
   then echo "RUNNING NOW"; exit
        else
        docker-compose -f full_path_to_project/docker-compose.yml -f full_path_to_project/docker-compose.prod.yml up -d
fi
'''


dayrestart_open = open("day_restart.sh", "w")
day_restart_write = dayrestart_open.write(dayrestart_str)
dayrestart_open.close()

healthcheck_open = open("healthcheck.sh", "w")
healcheck_write = healthcheck_open.write(healthcheck_str)
healthcheck_open.close()

# TODO add cron job daily restart, healtcheck min interval
