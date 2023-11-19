import argparse
import sys
import os
import omgdb.run_cmd 

def main():
    parser = argparse.ArgumentParser(
        prog=os.path.splitext(os.path.basename(sys.argv[0]))[0],
        description="Oh my GDB, an extension manager for gdb")
    valid_cmds=omgdb.run_cmd.valid_commands
    parser.add_argument('command', nargs='+', 
                        help="subcommand, available comands: %s"%(', '.join(valid_cmds)))
    args = parser.parse_args()
    cmd=args.command
    if cmd[0] == "help":
        parser.print_help()
        return
    omgdb.run_cmd.run_cmd(cmd)

if __name__=="__main__":
    main()
