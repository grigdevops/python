import locale

import yaml
import os


with open(r"server.yml") as file:
    servers = yaml.full_load(file)
    for item, doc in servers.items():
        print(item, doc)



for host in doc:
    response = os.system("ping -c 1 " + host)
    # and then check the response...
    if response == 0:
        print(host, 'is up!')
    else:
        print(host, 'is DOWN!')


