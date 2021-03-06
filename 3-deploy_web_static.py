#!/usr/bin/python3
"""
distribute an archive to web servers
"""
import os
import os.path
from time import strftime
from datetime import datetime
from fabric.api import *
from fabric.operations import run, put, sudo

env.hosts = ['66.70.184.29', '34.228.245.175']


def do_pack():
    ''' pack web_static directory into tgz archive
    '''
    try:
        time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static".format(time))
        return("versions/web_static_{}.tgz".format(time))
    except:
        return(None)


def do_deploy(archive_path):
    """that creates and distributes an archive to web servers"""

    if os.path.isfile(archive_path) is False:
        return False

    try:
        archive = archive_path.split('/')[-1]
        folder = archive.split('.')[0]
        strng = "data/web_static/releases"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}/".format(folder))
        run("sudo tar -xzf /tmp/{} -C /{}/{}/".format(archive, strng, folder))
        run("sudo rm /tmp/{}".format(archive))
        run("sudo mv /{0}/{1}/web_static/* /{0}/{1}/".format(strng, folder))
        run("sudo rm -rf /{}/{}/web_static".format(strng, folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /{}/{} /data/web_static/current".format(strng, folder))
        return True
    except Exception as e:
        return False


def deploy():
    """creates and distributes an archive to web servers"""
    try:
        pack = do_pack()
        d_deploy = do_deploy(pack)
        return(d_deploy)
    except:
        return(False)
