#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
"""
import os
from time import strftime
from datetime import datetime
from fabric.api import run, hosts, local


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
