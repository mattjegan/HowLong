from __future__ import absolute_import

import unittest
import sys

from HowLong import HowLong

def test_red():
    ret = HowLong.red("asdf")
    assert ret == '\033[91masdf\033[0m'


# While it would be good to also test the printed output,
# dealing with print statement versus print function
# being different across python2 and python3 makes that
# really hard.
class TestErrorAndExit(unittest.TestCase):
    def test_no_args(self):
        with self.assertRaises(SystemExit):
            HowLong.error_and_exit()

    def test_one_arg(self):
        with self.assertRaises(SystemExit):
            HowLong.error_and_exit("one")

    def test_multi_arg(self):
        with self.assertRaises(SystemExit):
            HowLong.error_and_exit("one", "two")
