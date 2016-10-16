from __future__ import print_function

import argparse
import logging
import sys

from datetime import timedelta
from subprocess import Popen
from time import time, sleep


def red(text):
    RED = '\033[91m'
    END = '\033[0m'
    return RED + text + END


class HowLong(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Time a process')
        parser.add_argument('-i', type=float, nargs='?', metavar='interval',
                            help='the timer interval, defaults to 1 second')
        parser.add_argument('-f', metavar='file', type=str, nargs=1,
                            help='output to file insted of stdout')
        parser.add_argument('-l', metavar='log level', nargs=1,
                            choices=['ERROR', 'INFO', 'DEBUG'],
                            help='set log level to ERROR/INFO/DEBUG')
        parser.add_argument('command', metavar='C', type=str, nargs='+',
                            help='a valid command')
        self.parsed_args = parser.parse_args()

        self.timer_interval = self.parsed_args.i if self.parsed_args.i else 1

        self.log_file = self.parsed_args.f[0] if self.parsed_args.f else None

        self.readable_command = " ".join(self.parsed_args.command)

        if self.parsed_args.l == ["ERROR"]:
            self.log_level = logging.ERROR
        elif self.parsed_args.l == ["DEBUG"]:
            self.log_level = logging.DEBUG
        else:
            self.log_level = logging.INFO

    def run(self):
        if self.log_file:
            logging.basicConfig(filename=self.log_file, level=self.log_level,
                                format='%(levelname)s:%(message)s')
        else:
            logging.basicConfig(level=self.log_level,
                                format='%(levelname)s:%(message)s')
        logging.debug("Running " + self.readable_command)

        process = Popen(self.parsed_args.command)
        start_time = time()
        while process.poll() is None:
            sleep(self.timer_interval)
            elapsed_time = (time() - start_time) * 1000
            logging.info(red(str(timedelta(milliseconds=elapsed_time))))

        logging.debug("Finished " + self.readable_command)


def howlong():
    HowLong().run()


if __name__ == "__main__": howlong()
