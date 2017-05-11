from __future__ import print_function

import argparse
import logging
import sys

from datetime import timedelta
from subprocess import Popen
from time import time, sleep
import psutil

def red(text):
    RED = '\033[91m'
    END = '\033[0m'
    return RED + text + END


class Process(object):
    def __init__(self,pid=None,command=None):
        self.pid = pid
        if self.pid is None:
            self.process = Popen(command)
            self.start_time = time()
        else:
            self.process = psutil.Process(self.pid)
            self.start_time = self.process.create_time()
            command = self.process.cmdline()
        self.command = ' '.join(command)

    def is_running(self):
        if self.pid is None:
            return self.process.poll() is None
        else:
            return self.process.is_running()

class HowLong(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Time a process')
        parser.add_argument('-i', type=float, nargs='?', metavar='interval',
                            help='the timer interval, defaults to 1 second')
        parser.add_argument('command', metavar='cmd', type=str, nargs=1,
                            help='a valid command')
        parser.add_argument('-f', metavar='file', type=str, nargs=1,
                            help='output to file insted of stdout')
        parser.add_argument('-l', metavar='log level', nargs=1,choices=['ERROR', 'INFO', 'DEBUG'],
                            help='set log level to ERROR/INFO/DEBUG')
        parser.add_argument('command_args', metavar='cmd_args', type=str,
                            nargs=argparse.REMAINDER,
                            help='additional arguments for target command')
        parsed_args = parser.parse_args()

        self.timer_interval = parsed_args.i if parsed_args.i else 1

        self.command = parsed_args.command + parsed_args.command_args
        self.readable_command = ' '.join(self.command)
        self.log_file = parsed_args.f[0] if parsed_args.f else None

        if parsed_args.command == ['pid']:
            self.pid = int(parsed_args.command_args[0])
            assert self.pid in psutil.pids(), "argument p must be a valid pid, %d is not one" % pid
        else:
            self.pid = None


        if parsed_args.l == ["ERROR"]:
            self.log_level = logging.ERROR
        elif parsed_args.l == ["DEBUG"]:
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

        process = Process(pid=self.pid,command=self.command)
        readable_command = process.command
        start_time = process.start_time
        logging.debug("Running " + readable_command)
        while process.is_running():
            sleep(self.timer_interval)
            elapsed_time = (time() - start_time) * 1000
            logging.info(red(str(timedelta(milliseconds=elapsed_time))))
        logging.debug("Finished " + self.readable_command)


def howlong():
    HowLong().run()


if __name__ == "__main__": howlong()
