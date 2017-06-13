#!/usr/bin/python3
"""Unittest for file_storage.py
"""
import unittest
import uuid
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    'class for testing FileStorage'


    def setUp(self):
        'called multiple times, once before each test'
        self.new_inst = FileStorage()

    def tearDown(self):
        'called multiple times, once after each test'
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test_all(self):
        'test correct return for all: __objects'
        explicit = self.new_inst._FileStorage__objects
        implicit = self.new_inst.all()
        self.assertEqual(explicit, implicit)

    def test_new(self):
        'test that a new object is added to __objects'


    def test_save(self):
        'test that __object was serialized to JSON file'
        

    def test_reload(self):
        'test that JSON file was deserialized to __objects'


if __name__ == '__main__':
    unittest.main()
