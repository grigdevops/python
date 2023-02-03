import yaml
import os
import subprocess


def ping(host):
    response = os.system('ping -c 1 ' + host)
    if response == 0:
        return True
    else:
        return False

def main():
    with open("servers.yaml", "r") as file:
        config = yaml.safe_load(file)

    down_devices = []
    for device in config["devices"]:
        host = device["ip_address"]
        if not ping(host):
            down_devices.append(device["hostname"])

    with open("down_devices.yaml", "w") as file:
        for host in down_devices:
            file.write(host + "\n")

if __name__ == "__main__":
    main()