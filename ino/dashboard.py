import os, sys


import os
import sys

username = sys.argv[1]
password = sys.argv[2]

path = "/root/dashboard"
isFilePath = os.path.exists(path)
if isFilePath:
    os.system(f"cd {path} && git pull")
    print("es mekan")
else:
    os.system(f"git clone http://{username}:{password}@git.inorain.com/inorain/inorain.tv/dashboard.git")
    os.system("cd dashboard && docker build -t dashboard_image .")