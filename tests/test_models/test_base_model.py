#!/usr/bin/python3
"""Unittest for base_model.py
"""
import unittest
import uuid
import os
import models
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    'class for testing base_model'


    def setUp(self):
        'called multiple times, once before each test'
        self.new_inst = BaseModel()

    def tearDown(self):
        'called multiple times, once after each test'
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass
    
    def test__init__id(self):
        'tests __init__: id'
        this_dict = self.new_inst.__dict__
        self.assertIsNotNone(this_dict.get("id"))

    def test__init__created_at(self):
        'tests __init__: created_at'
        this_dict = self.new_inst.__dict__
        self.assertIsNotNone(this_dict.get("created_at"))

    def test_attributes(self):
        'tests for attributes'
        self.assertFalse(hasattr(self.new_inst, "updated_at"))
        self.assertFalse(hasattr(self.new_inst, "my_number"))
        self.assertFalse(hasattr(self.new_inst, "random_attr"))
        self.new_inst.name = "TeamTeam!"
        self.new_inst.age = 100
        self.assertTrue(hasattr(self.new_inst, "name"))
        self.assertEqual(self.new_inst.name, "TeamTeam!")
        self.assertTrue(hasattr(self.new_inst, "age"))
        delattr(self.new_inst, "name")
        self.assertFalse(hasattr(self.new_inst, "name"))
        self.assertEqual(self.new_inst.__class__.__name__, "BaseModel")

    def test_save_init(self):
        'test to make sure no "updated_at" is created upon creation'
        this_dict = self.new_inst.__dict__
        # this_dict = storage.all()
        print("this_dict: {}".format(this_dict))
        self.assertIsNone(this_dict.get("updated_at"))

    def test_save_update(self):
        'tests save: updating a file'
        this_dict = self.new_inst.__dict__
        # this_dict = storage.all()
        print("this_dict (before save): {}".format(this_dict))
        before = this_dict.get("updated_at")
        self.new_inst.save()
        this_dict = self.new_inst.__dict__
        # this_dict = storage.all()
        print("this_dict (after save): {}".format(this_dict))
        after = this_dict.get("updated_at")
        self.assertNotEqual(before, after)
        
    def test___str__(self):
        'test __str__: check format'
        correct_format = ("[{}] ({}) {}".format(self.new_inst.__class__.__name__,
                                                self.new_inst.id,
                                                self.new_inst.__dict__))
        self.assertEqual(print(correct_format), print(self.new_inst))

    def test_to_json(self):
        'test to_json'
        json_return = BaseModel.to_json(self.new_inst)
        self.assertEqual(type(json_return), dict)

if __name__ == '__main__':
    unittest.main()
