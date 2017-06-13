#!/usr/bin/python3
"""Unittest for amenity.py
"""
import unittest
import uuid
import os
import models
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    'class for testing amenity'


    def setUp(self):
        'called multiple times, once before each test'
        self.new_inst = Amenity()

    def tearDown(self):
        'called multiple times, once after each test'
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    
    def test__init__id(self):
        'tests __init__: id'
        this_dict = self.new_amenity.__dict__
        self.assertIsNotNone(this_dict.get("id"))

    def test__init__created_at(self):
        'tests __init__: created_at'
        this_dict = self.new_amenity.__dict__
        self.assertIsNotNone(this_dict.get("created_at"))

    def test_attributes(self):
        'tests for attributes'
        self.assertTrue(hasattr(self.new_amenity, "name"))
        self.assertEqual(self.new_amenity.name, "")

        self.assertFalse(hasattr(self.new_amenity, "updated_at"))
        self.assertFalse(hasattr(self.new_amenity, "my_number"))
        self.assertFalse(hasattr(self.new_amenity, "random_attr"))
        self.new_amenity.name = "TeamTeam!"
        self.new_amenity.age = 100
        self.assertTrue(hasattr(self.new_amenity, "name"))
        self.assertEqual(self.new_amenity.name, "TeamTeam!")
        self.assertTrue(hasattr(self.new_amenity, "age"))
        delattr(self.new_amenity, "name")
        self.assertFalse(hasattr(self.new_amenity, "name"))
        self.assertEqual(self.new_amenity.__class__.__name__, "BaseModel")

    def test_save_init(self):
        'test to make sure no "updated_at" is created upon creation'
        this_dict = self.new_amenity.__dict__
        # this_dict = storage.all()
        print("this_dict: {}".format(this_dict))
        self.assertIsNone(this_dict.get("updated_at"))

    def test_save_update(self):
        'tests save: updating a file'
        this_dict = self.new_amenity.__dict__
        # this_dict = storage.all()
        print("this_dict (before save): {}".format(this_dict))
        before = this_dict.get("updated_at")
        self.new_amenity.save()
        this_dict = self.new_amenity.__dict__
        # this_dict = storage.all()
        print("this_dict (after save): {}".format(this_dict))
        after = this_dict.get("updated_at")
        self.assertNotEqual(before, after)
        
    def test___str__(self):
        'test __str__: check format'
        correct_format = ("[{}] ({}) {}".format(self.new_amenity.__class__.__name__,
                                                self.new_amenity.id,
                                                self.new_amenity.__dict__))
        self.assertEqual(print(correct_format), print(self.new_amenity))

    def test_repr(self):
        str_return = self.new_amenity.__str__
        self.assertIsNotNone(str_return)

    def test_to_json(self):
        'test to_json'
        json_return = BaseModel.to_json(self.new_amenity)
        self.assertEqual(type(json_return), dict)

if __name__ == '__main__':
    unittest.main()
