#!/usr/bin/env python3
if __package__:
    from .options import Options
    from .prompt import Prompt
else:
    from options import Options
    from prompt import Prompt
import importlib
import sys

def main():
    """ Main execution thread """

    options = Options().load_options()
    prompt = Prompt(options)
    prompt.prompt = 'falconbot> '
    prompt.cmdloop('[+] Starting falconbot interface...')

if __name__ == "__main__":
    sys.exit(main())
