#!/usr/bin/python3
'Test for console.py'

from unittest.mock import create_autospec
from console import HBNBCommand
import unittest
import sys

class TestConsole(unittest.TestCase):
    'test console.py'
    def setUp(self):
        'setUp mock stdin and stdout'
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        'test create'
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_exit(self):
        'test exit'
        cmd = self.create()
        self.assertRaises(SystemExit, quit)
