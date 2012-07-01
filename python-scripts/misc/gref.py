import subprocess

def run(arg):
    grep_command = "grep -n -H -r '{}' *".format(arg)
    print grep_command
    less_command = 'less'

    grep = subprocess.Popen(grep_command, shell = True, stdout = subprocess.PIPE)
    subprocess.check_call(less_command, stdin=grep.stdout, shell = True)
