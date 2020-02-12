""" Interactive Prompt """

if __package__:
    from .options import Options
else:
    from options import Options
import sys
from cmd import Cmd

class Prompt(Cmd, object):
    """ Handle user input """

    def __init__(self, options):
        super(Prompt, self).__init__()

        self.options = options

    def do_options(self, args):
        """ List loaded options """

        for key in self.options:
            print("  " + str(key) + ": " + str(self.options[key]))

    def do_quit(self, args):
        """ Quit the program """

        print("[+] Shutting down")

        raise SystemExit
