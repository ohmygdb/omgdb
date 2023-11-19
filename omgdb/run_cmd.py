import sys
import omgdb.init
import omgdb.list_modules
import omgdb.enable
import omgdb.disable
import omgdb.update
import omgdb.search 

commands={ 'init':omgdb.init.main,
           'list':omgdb.list_modules.main,
           'enable':omgdb.enable.main,
           'disable':omgdb.disable.main,
           'update':omgdb.update.main,
           'search':omgdb.search.main }
valid_commands=list(commands.keys())

def run_cmd(command):
    cmd=command[0]
    argv=command[1:]
    if cmd not in valid_commands:
        print("Unrecognized command: %s"%(cmd,))
        exit(1)
    commands[cmd](argv)
