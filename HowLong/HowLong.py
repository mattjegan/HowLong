import argparse
from datetime import timedelta
from subprocess import Popen
from sys import argv, exit
from time import time, sleep

RED = '\033[91m'
END = '\033[0m'

class HowLong:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Time a process')
        parser.add_argument('command', metavar='C', type=str, nargs='+',
                            help='a valid command')
        parsed_args = parser.parse_args()

        self.command = " ".join(parsed_args.command)

    def run(self):
        print("Running", self.command)
        process = Popen(argv[1:])
        start_time = time()

        while process.poll() is None:
            sleep(1)
            print(RED + str(timedelta(seconds=int(time() - start_time))) + END)

        print("Finished", self.command)

if __name__ == "__main__": HowLong().run()