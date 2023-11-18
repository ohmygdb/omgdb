import sys
import omgdb

commands={ 'init':omgdb.init,
           'list':omgdb.list_modules,
           'enable':omgdb.enable,
           'disable':omgdb.disable,
           'update':omgdb.update,
           'search':omgdb.search }
valid_commands=list(commands.keys())

def run_cmd(command):
    cmd=command[0]
    argv=command[1:]
    if cmd not in valid_commands:
        print("Unrecognized command: %s"%(cmd,))
        exit(1)
    print("args: %s"%(argv,))
