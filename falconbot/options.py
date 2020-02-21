""" Configuration loading and argument handling """

import argparse
import configparser
import sys
import os

class Options(object):
    """ Option-handling Object """

    def __init__(self):
        self.options = {}

    def parse_args(self):
        """ Parse optional arguments """

        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--config", dest="config", default="/etc/falconbot/conf/falconbot.conf", type=str, help="path to config file")
        parser.add_argument("-e", "--environment", dest="environment", default="DEFAULT", type=str, help="config environment")
        parser.add_argument("-p", "--password", dest="password", type=str, help="account password")
        parser.add_argument("-s", "--service", dest="service", type=str, help="target service")
        parser.add_argument("-t", "--token", dest="token", type=str, help="API token")
        parser.add_argument("-u", "--username", dest="username", type=str, help="account name")
        args = parser.parse_args()

        return args

    def load_options(self):
        """ Load options and overrides """

        args = self.parse_args()
        conf = configparser.ConfigParser()

        print("[+] Reading configuration file")
        try:
            conf.read(args.config)
            print("[+] Loading options from file")
            for key in conf[args.environment]:
                self.options[key] = conf[args.environment][key]
        except Exception as e:
            sys.exit("Unable to read config file, does it exist?")

        print("[+] Loading environment variable overrides")
        for arg in vars(args):
            if arg.upper() in os.environ:
                self.options[arg] = os.environ[arg.upper()]

        print("[+] Loading argument overrides")
        for arg in vars(args):
            if getattr(args, arg) is not None:
                self.options[arg] = getattr(args, arg)

        return self.options
