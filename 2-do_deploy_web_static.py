#!/usr/bin/python3
"""
deployment of compressed web_static archive to both servers
store file in specified directory and decompress
"""

from fabric.api import *
from fabric.context_managers import cd
from os import path

env.hosts = ['34.224.94.62', '35.168.3.19']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    upload archive file to directory, then uncompress in different\
    directory
    delete the archive
    deletes current symbolic link of /data/web_static/current
    creates a new symbolic link

    Args:
    archive_path (str): path to archive on local

    Return:
    True on success, else False
    """
    try:
        if archive_path is None:
            return (False)

        put(archive_path, "/tmp/")

        """getting folder name without extension"""
        foldername = archive_path[9:-4]
        arch_filename = archive_path[9:]
        run("sudo mkdir -p /data/web_static/releases/{}".format(
            foldername))
        run("sudo tar -xzf /tmp/{} -C /data/\
web_static/releases/{}/".format(arch_filename, foldername))

        run("sudo rm /tmp/{}".format(arch_filename))
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/\
web_static/releases/{}".format(foldername, foldername))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(
            foldername))

        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}\
            /data/web_static/current".format(foldername))
    except Exception:
        return (False)

    return (True)
