import os
import inquirer
import argparse
import pathlib
import platform


def write_init(path,modules,interactive=False):
    with open(path, 'a') as file:
        pass
    
def get_path_choices():
    os_type = platform.system()
    if(os_type=='Linux'):
        return ['$XDG_CONFIG_HOME/gdb/gdbinit',
        '$HOME/.config/gdb/gdbinit',
        '$HOME/.gdbinit']
    elif os_type=='Darwin':
        return ['$HOME/Library/Preferences/gdb/gdbinit',
                 '$HOME/.gdbinit']
    elif os_type=='Windows':
        raise OSError("Windows is not supported by omgdb.")
def main(**kwargs):
    try:
        path=kwargs['path']
    except KeyError:
        path='~/.config/gdb/'
    try:
        interactive=kwargs['interactive']
    except KeyError:
        interactive=False
    questions=[
        inquirer.List('init_path',
                      message='Where should your init file be stored?',
                      choices=get_path_choices()),
        inquirer.Checkbox('modules',
                          message='Which modules would you like to add initially (more can be added later?',
                          choices=['prompt_simple',
                                   'prompt_powerline',
                                   'prettyprint_cpp',
                                   'history',
                                   'assembly',
                                   'alias_windbg'])
    ]
    modules=['history']
    if(interactive):
        answers=inquirer.prompt(questions)
        path=answers['init_path']
        modules=answers['modules']
    write_init(path,modules,interactive)
