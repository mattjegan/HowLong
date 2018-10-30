from __future__ import absolute_import

import os
import sys
import unittest


from HowLong.HowLong import Process

class TestProcess(unittest.TestCase):
    def test_command(self):
        p = Process(command=["true"])
        assert p.command == "true"
        assert p.start_time

    def test_pid(self):
        p = Process(os.getpid())
        # Specific command could be dependent on host running test,
        # settle for making sure it was filled in at all.
        assert p.command
        assert p.start_time

    def test_is_running_pid(self):
        p = Process(os.getpid())
        assert p.is_running()

    def test_is_running_cmd(self):
        p = Process(command=["true"])
        assert p.is_running()
