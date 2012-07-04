import subprocess
import os

CYAN = os.environ["ECHO_CYAN"]
DEFAULT = os.environ["ECHO_DEFAULT"]
PURPLE = os.environ["ECHO_PURPLE"]

def run():
    source = "{}{sep}vim".format(os.environ["KFS_SETTINGS"], sep=os.sep)
    home = os.environ["HOME"]

    oldrc = "{}{sep}.vimrc".format(home, sep=os.sep)
    olddotvim ="{}{sep}.vim".format(home, sep=os.sep)

    if os.path.exists(oldrc):
        with open(oldrc) as f:
            line = f.readline()
            if line[:-1] == '" --- KFS VIM SETTINGS ---':
                return
        make_backup(oldrc)
        make_backup(olddotvim)

    command = "cp {source}{sep}vimrc {path}{sep}.vimrc".format(source=source, sep=os.sep, path=home)
    subprocess.check_call(command, shell=True)

    command = "cp -r {source}{sep}.vim {path}".format(source=source, sep=os.sep, path=home)
    subprocess.check_call(command, shell=True)

def make_backup(path):
    backup = "{}.backup".format(path)
    command = "echo 'Making backup of file(s):: {cyan}{f} {default}({purple}{backup}{default})'"
    command = command.format(cyan=CYAN, f=path, default=DEFAULT, purple=PURPLE, backup=backup)
    subprocess.check_call(command, shell=True)
    command = "mv {f} {backup}".format(f=path, backup=backup)
    subprocess.check_call(command, shell=True)

if __name__ == "__main__":
    run()
