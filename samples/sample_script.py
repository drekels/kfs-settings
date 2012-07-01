import subprocess

def run(arg):
    command = "echo Hello {}".format(arg)
    print command

    subprocess.check_call(command, shell = True)
