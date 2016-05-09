#!/usr/bin/env python3

__author__ = "Matthew Egan"

from datetime import timedelta
from subprocess import Popen
from sys import argv
from time import time, sleep

RED = '\033[91m'
END = '\033[0m'

class HowLong:
    def __init__(self):
        self.command = " ".join(argv[1:])

    def run(self):
        print("Running", self.command)
        process = Popen(argv[1:])
        start_time = time()

        while process.poll() is None:
            sleep(1)
            print(RED + str(timedelta(seconds=int(time() - start_time))) + END)

        print("Finished", self.command)

if __name__ == "__main__": HowLong().run()