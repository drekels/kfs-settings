import subprocess
import os
from util.repository import foreach_dir

def run(*args):
    foreach_dir(commit, is_svn_dir, os.getcwd(), args)

def is_svn_dir(directory):
    return ".svn" in os.listdir(directory)

def commit(working, *args):
    relative_path = working.replace(os.getcwd(), "")
    if relative_path[0] == os.sep:
        relative_path = relative_path[1:]
    command = "svn status {}".format(" ".join(args))
    print " >>> {} >>> {}".format(relative_path, command)
    subprocess.check_call(command, cwd = working, shell = True)
