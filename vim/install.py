#!/usr/bin/python2.7


import subprocess
import os


CYAN = os.environ["ECHO_CYAN"]
DEFAULT = os.environ["ECHO_DEFAULT"]
PURPLE = os.environ["ECHO_PURPLE"]


HOME = os.environ["HOME"]
HOME_VIMRC = os.path.join(HOME, ".vimrc")
HOME_VIM_FILES = os.path.join(HOME, ".vim")
KFS_SETTINGS = os.environ["KFS_SETTINGS"]
KFS_VIM = os.path.join(KFS_SETTINGS, "vim")
KFS_VIMRC = os.path.join(KFS_VIM, "vimrc")
KFS_VIM_FILES = os.path.join(KFS_VIM, "vim_files")


def main():
    vimrc()
    vim_files()


def vimrc():
    with open(HOME_VIMRC, "w") as f:
        f.write("source {}".format(KFS_VIMRC))


def vim_files():
    subprocess.check_call("rm -f {}".format(HOME_VIM_FILES), shell=True)
    subprocess.check_call("ln -s {} {}".format(KFS_VIM_FILES, HOME_VIM_FILES), shell=True)


if __name__ == "__main__":
    main()
