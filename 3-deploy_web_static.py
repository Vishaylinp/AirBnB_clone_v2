#!/usr/bin/python3
"""
fabric script that generates an archive of web_static folder
and store this archive with a specified format in 'versions'
folder
"""

from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['34.224.94.62', '35.168.3.19']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
    Adds all files in 'web_static' directory to final archive
    creates and stores archive in 'versions' directory with \
    specified name format

    Return:
    path of archive on success, else None
    """

    """datetime for name of archive file"""
    cur_dt = datetime.now()
    y = cur_dt.year
    mh = cur_dt.month
    d = cur_dt.day
    h = cur_dt.hour
    mt = cur_dt.minute
    s = cur_dt.second

    filename = "web_static_{}{}{}{}{}{}.tgz".format(
        y, mh, d, h, mt, s)
    print(filename)

    try:
        fa.local("mkdir -p versions")
        fa.local("tar -czvf versions/{} web_static/".format(
            filename))
        return ("versions/{}".format(filename))

    except Exception as e:
        return (None)


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


def deploy():
    """creates and deploys an archive to webservers"""
    my_file = do_pack()
    if my_file is None:
        return (False)
    return do_deploy(my_file)
