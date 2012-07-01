import subprocess


def run(*message):
    assert(len(message) > 0)
    m = " ".join(message)
    command = "git commit -m '{}'".format(m)
    print command
    subprocess.check_call(command, shell = True)







