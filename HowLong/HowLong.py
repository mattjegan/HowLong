from __future__ import print_function

import argparse
import logging
import sys

from datetime import timedelta
from subprocess import Popen
from time import time, sleep
import psutil

def exception_handler(exception_type, exception, traceback):
    '''hide traceback'''
    print ("%s" % exception)
sys.excepthook = exception_handler

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
        parser.add_argument('-c', metavar='command', type=str, nargs=1,
                            help='a valid command')
        parser.add_argument('-p', metavar='pid', type=int, nargs=1,
                            help='a valid process id to monitor - see \'ps aux\'')
        parser.add_argument('-f', metavar='file', type=str, nargs=1,
                            help='output to file insted of stdout')
        parser.add_argument('-l', metavar='log level', nargs=1,
                            choices=['ERROR', 'INFO', 'DEBUG'],
                            help='set log level to ERROR/INFO/DEBUG')
        parser.add_argument('command_args', metavar='cmd_args', type=str,
                            nargs=argparse.REMAINDER,
                            help='additional arguments for target command')
        parsed_args = parser.parse_args()

        self.timer_interval = parsed_args.i if parsed_args.i else 1

        command = parsed_args.c if parsed_args.c else None
        cmd_args = parsed_args.command_args if parsed_args.command_args else None
        assert command is not None or cmd_args is None, "Can't have no command but have command args, \
                             usage with command is: howlong [options] -c your_command your_options"
        if parsed_args.p:
            self.pid = int(parsed_args.p[0])
            self.command = None
            assert command is None, "can't have both -p and -c"
            assert self.pid in psutil.pids(), "argument p must be a valid pid, %d is not one" % pid
        else:
            assert command is not None, "you must use either -p or -c"
            self.pid = None
            cmd_args = [] if cmd_args is None else cmd_args
            self.command = command + cmd_args
        
        self.log_file = parsed_args.f[0] if parsed_args.f else None
        
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
        logging.debug("Finished " + readable_command)


def howlong():
    HowLong().run()


if __name__ == "__main__": howlong()
