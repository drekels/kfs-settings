import os

def foreach_dir(func, check, start, args, stop_on_check=True):
    will_continue = True

    if check(start):
        will_continue = not stop_on_check
        func(start, *args)

    if will_continue:
        paths = ["{}{}{}".format(start, os.sep, x) for x in os.listdir(start)]
        for directory in [path for path in paths if os.path.isdir(path)]:
            foreach_dir(func, check, directory, args, stop_on_check)
