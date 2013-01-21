import sys
import os

def find_module(name):
    for directory, _, names in os.walk(os.environ["PYTHON_SCRIPTS"]):
        for n in names:
            s = n.split('.')
            if len(s) == 2 and s[0] == name and s[1] == 'py':
                path = directory.split(os.sep)[-1].replace(os.sep, ".") + "." + name
                return getattr(__import__(path), name)
    raise Exception("Could not find script '{}'".format(name))

if __name__ == "__main__":
    script = sys.argv[1]
    args = sys.argv[2:]
    module = find_module(script)
    module.run(*args)

