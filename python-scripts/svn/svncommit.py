import subprocess
import os
from util.repository import foreach_dir

def run(*message):
    assert(len(message) > 0)
    message = " ".join(message)
    foreach_dir(commit, is_svn_dir, os.getcwd(), [message])

def is_svn_dir(directory):
    return ".svn" in os.listdir(directory)

def commit(working, message):
    command = "svn commit -m '{}'".format(message)
    subprocess.check_call(command, cwd = working, shell = True)
