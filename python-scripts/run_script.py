import sys

scripts = {
           'gcommit'       : ['git', 'gcommit'],
           'grollback'     : ['git', 'grollback'],
           'grebase'       : ['git', 'grebase'],
           'review_post'   : ['review', 'review_post'],
           'review_update' : ['review', 'review_update'],
           'unittest'      : ['emc', 'unittest'],
           'gref'          : ['misc', 'gref'],
          }

if __name__ == "__main__":
    script = sys.argv[1]
    args = sys.argv[2:]
    path = scripts[script]
    module = __import__(".".join(path))
    for m in path[1:]:
        module = getattr(module, m)
    module.run(*args)



