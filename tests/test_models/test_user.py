#!/usr/bin/python3
"""Unittest for user.py
"""
import unittest
import uuid
import os
from models.user import User
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    'class for testing user'

    def setUp(self):
        'called multiple times, once before each test'
        self.new_user = User()

    def tearDown(self):
        'called multiple times, once after each test'
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test__init__id(self):
        'tests __init__: id'
        this_dict = self.new_user.__dict__
        self.assertIsNotNone(this_dict.get("id"))

    def test__init__created_at(self):
        'tests __init__: created_at'
        this_dict = self.new_user.__dict__
        self.assertIsNotNone(this_dict.get("created_at"))

    def test_attributes(self):
        'tests for attributes'
        self.assertTrue(hasattr(self.new_user, "email"))
        self.assertEqual(self.new_user.email, "")
        self.assertTrue(hasattr(self.new_user, "password"))
        self.assertEqual(self.new_user.email, "")
        self.assertTrue(hasattr(self.new_user, "first_name"))
        self.assertEqual(self.new_user.email, "")
        self.assertTrue(hasattr(self.new_user, "last_name"))
        self.assertEqual(self.new_user.email, "")

        self.assertFalse(hasattr(self.new_user, "updated_at"))
        self.assertFalse(hasattr(self.new_user, "my_number"))
        self.assertFalse(hasattr(self.new_user, "random_attr"))
        self.new_user.name = "TeamTeam!"
        self.new_user.age = 100
        self.assertTrue(hasattr(self.new_user, "name"))
        self.assertEqual(self.new_user.name, "TeamTeam!")
        self.assertTrue(hasattr(self.new_user, "age"))
        delattr(self.new_user, "name")
        self.assertFalse(hasattr(self.new_user, "name"))
        self.assertEqual(self.new_user.__class__.__name__, "BaseModel")

    def test_save_init(self):
        'test to make sure no "updated_at" is created upon creation'
        this_dict = self.new_user.__dict__
        # this_dict = storage.all()
        print("this_dict: {}".format(this_dict))
        self.assertIsNone(this_dict.get("updated_at"))

    def test_save_update(self):
        'tests save: updating a file'
        this_dict = self.new_user.__dict__
        # this_dict = storage.all()
        print("this_dict (before save): {}".format(this_dict))
        before = this_dict.get("updated_at")
        self.new_user.save()
        this_dict = self.new_user.__dict__
        # this_dict = storage.all()
        print("this_dict (after save): {}".format(this_dict))
        after = this_dict.get("updated_at")
        self.assertNotEqual(before, after)

    def test___str__(self):
        'test __str__: check format'
        correct_format = ("[{}] ({}) {}".format
                          (self.new_user.__class__.__name__,
                           self.new_user.id,
                           self.new_user.__dict__))
        self.assertEqual(print(correct_format), print(self.new_user))

    def test_repr(self):
        str_return = self.new_user.__str__
        self.assertIsNotNone(str_return)

    def test_to_json(self):
        'test to_json'
        json_return = BaseModel.to_json(self.new_user)
        self.assertEqual(type(json_return), dict)

if __name__ == '__main__':
    unittest.main()
