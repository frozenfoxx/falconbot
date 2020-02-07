#!/usr/bin/env python3
if __package__:
    from .options import Options
else:
    from options import Options
import importlib
import sys

def main():
    """ Main execution thread """

    options = Options().load_options()


if __name__ == "__main__":
    sys.exit(main())
