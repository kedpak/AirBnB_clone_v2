#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
"""
import os
import os.path
from time import strftime
from datetime import datetime
from fabric.api import *
from fabric.operations import run, put, sudo

env.hosts = ['66.70.184.29', '34.228.245.175']

def do_deploy(archive_path):


    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split('/')[-1]
        folder = archive.split('.')[0]
        print('before put')
        put(archive_path, "/tmp/")
        print('after put')
        run("sudo mkdir -p /data/web_static/releases/{}/".format(folder))
        run("sudo tar -xzf /tmp/ {} -C /data/web_static/releases/{}/".format(archive, folder))
        run("sudo rm /tmp/{}".format(archive))
        run("sudo mv /data/web_static/releases/{}/* /data/web_static/releases/{}/".format(folder, folder))
        run("sudo rm -rf /data/web_static/releases{}/web_static".format(folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} /data/web_static/current".format(folder))
        return True
    except Exception as e:
        print(e)
        return False
