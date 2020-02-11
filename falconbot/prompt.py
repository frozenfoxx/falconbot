""" Interactive Prompt """

import sys
from cmd import Cmd

class Prompt(Cmd, object):
    """ Handle user input """

    def __init__(self):

    def do_quit(self, args):
        """ Quit the program """

        print("[+] Shutting down")

        raise SystemExit
