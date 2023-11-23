import os
import inquirer
import argparse
import pathlib

    

def main(**kwargs):
    try:
        path=kwargs['path']
    except KeyError:
        path='~/.config/gdb/'
    try:
        interactive=kwargs['interactive']
    except KeyError:
        interactive=False
