#!/usr/bin/python -i
import readline
import os
import rlcompleter
import atexit


PYHIST = os.environ['PYTHONHISTORY']


try:
    readline.read_history_file(PYHIST)
except IOError:
    pass
readline.parse_and_bind('tab: complete')
atexit.register(readline.write_history_file, PYHIST)


del PYHIST, readline, os, rlcompleter, atexit
