import subprocess

def run(arg):
    try:
        arg = "HEAD~{}".format(int(arg))
    except:
        pass
    command = "git rebase -i {}".format(arg)
    print command
    subprocess.check_call(command, shell = True)
