#!/usr/bin/python2.7

import subprocess
import os

libdir = "/usr/lib/python2.7/pykfs"
kfs_settings = os.path.dirname(os.path.abspath(__file__))
print kfs_settings

subprocess.check_call("rm {}".format(libdir), shell=True)
subprocess.check_call("ln -s {}/pykfs {}".format(kfs_settings, libdir), shell=True)
