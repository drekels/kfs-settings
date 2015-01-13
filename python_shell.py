#!/usr/bin/python -i

import os
import rlcompleter
import atexit


PYHIST = os.environ['PYTHONHISTORY']


try:
    import readline
    try:
        readline.read_history_file(PYHIST)
    except IOError:
        pass
    readline.parse_and_bind('tab: complete')
    atexit.register(readline.write_history_file, PYHIST)
    del PYHIST, readline, os, rlcompleter, atexit
except ImportError:
    pass

def pretty(value):
    import json
    return json.dumps(value, indent=4)
