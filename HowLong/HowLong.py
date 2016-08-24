import argparse
from datetime import timedelta
from subprocess import Popen
from time import time, sleep

RED = '\033[91m'
END = '\033[0m'

class HowLong(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Time a process')
        parser.add_argument('-i', type=float, nargs='?', metavar='interval',
                            help='the timer interval, defaults to 1 second')
        parser.add_argument('command', metavar='C', type=str, nargs='+',
                            help='a valid command')
        self.parsed_args = parser.parse_args()

        self.timer_interval = self.parsed_args.i if self.parsed_args.i else 1

        self.readable_command = " ".join(self.parsed_args.command)

    def run(self):
        print("Running", self.readable_command)

        process = Popen(self.parsed_args.command)
        start_time = time()
        while process.poll() is None:
            sleep(self.timer_interval)
            elapsed_time = (time() - start_time) * 1000
            print(RED + str(timedelta(milliseconds=elapsed_time)) + END)

        print("Finished", self.readable_command)

def howlong():
    HowLong().run()

if __name__ == "__main__": howlong()