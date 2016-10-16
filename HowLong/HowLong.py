from __future__ import print_function

import argparse
import sys

from datetime import timedelta
from subprocess import Popen
from time import time, sleep


def red(text):
    RED = '\033[91m'
    END = '\033[0m'
    return RED + text + END


def log(*args):
    print(*args, file=sys.stderr)
    sys.stderr.flush()


class HowLong(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Time a process')
        parser.add_argument('-i', type=float, nargs='?', metavar='interval',
                            help='the timer interval, defaults to 1 second')
        parser.add_argument('command', metavar='cmd', type=str, nargs=1,
                            help='a valid command')
        parser.add_argument('command_args', metavar='cmd_args', type=str,
                            nargs=argparse.REMAINDER,
                            help='additional arguments for target command')
        parsed_args = parser.parse_args()

        self.timer_interval = parsed_args.i if parsed_args.i else 1

        self.command = parsed_args.command + parsed_args.command_args
        self.readable_command = ' '.join(self.command)

    def run(self):
        log("Running", self.readable_command)

        process = Popen(self.command)
        start_time = time()
        while process.poll() is None:
            sleep(self.timer_interval)
            elapsed_time = (time() - start_time) * 1000
            log(red(str(timedelta(milliseconds=elapsed_time))))

        log("Finished", self.readable_command)


def howlong():
    HowLong().run()


if __name__ == "__main__": howlong()
