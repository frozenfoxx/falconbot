#!/usr/bin/env python3

import importlib
import sys
from options import Options

def main():
    """ Main execution thread """

    options = Options().load_options()


if __name__ == "__main__":
    sys.exit(main())
