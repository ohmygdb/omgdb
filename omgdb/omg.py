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
    parser.add_argument('-i','--interactive', action='store_true', default=False,
                        help="Run subcommand interactively")
    args = parser.parse_args()
    if args.command[0] == "help":
        parser.print_help()
        exit(0)
    omgdb.run_cmd.run_cmd(cmd=args.command[0],
                          interactive=args.interactive,
                          argv=args.command[1:])

if __name__=="__main__":
    main()
