import locale

import yaml
import os


with open(r"server.yml") as file:
    servers = yaml.full_load(file)
    for routers, hostname in servers.items():
        print(routers, hostname)



for host in hostname:
    response = os.system("ping -c 1 " + host)
    # and then check the response...
    if response == 0:
        print(host, 'is up!')
    else:
        print(host, 'is DOWN!')


