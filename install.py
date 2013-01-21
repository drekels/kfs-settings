#!/usr/bin/python2.7

import subprocess

libdir = "/usr/lib/python2.7/pykfs"
subprocess.check_call("ln -s $KFS_SETTINGS/pykfs {}".format(libdir), shell=True)
