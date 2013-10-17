import json
import subprocess

def run(arg):
    with open(arg) as f:
        obj = json.load(f)
        s = json.dumps(obj, indent=4)
    process = subprocess.Popen("less", stdin=subprocess.PIPE)
    process.communicate(s);
