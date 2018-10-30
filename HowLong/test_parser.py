from __future__ import absolute_import

import unittest
from HowLong.HowLong import HowLong

class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''sets up the initial config'''
        cls.parser = HowLong

    def test_empty_arguments(self):
        '''Tests with no arguments
            At least one argument is required.
        '''
        with self.assertRaises(SystemExit):
            self.parser()

    def test_c_option_with_empty_arguments(self):
        '''Tests with c argument
            At least one command is required.
        '''
        with self.assertRaises(TypeError):
            self.parser('-c')

    def test_p_option_with_empty_arguments(self):
        '''Tests with p argument
            At least one process is required.
        '''
        with self.assertRaises(TypeError):
            self.parser('-p')
