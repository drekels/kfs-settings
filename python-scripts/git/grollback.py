
import subprocess


def run(*args):
    assert (len(args) == 1 or len(args) == 0)
    count = 1
    if args:
        count = args[0]
    command = "git reset --hard HEAD~{}".format(count)
    
    subprocess.check_call(command, shell = True)
