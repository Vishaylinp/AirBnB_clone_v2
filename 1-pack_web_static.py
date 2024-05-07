#!/usr/bin/python3
"""
fabric script that generates an archive of web_static folder
and store this archive with a specified format in 'versions'
folder
"""

import fabric.api as fa
from datetime import datetime


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
