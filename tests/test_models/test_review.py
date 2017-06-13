#!/usr/bin/python3
"""Unittest for review.py
"""
import unittest
import uuid
import os
import models
from models import storage
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    'class for testing review'


    def setUp(self):
        'called multiple times, once before each test'
        self.new_review = Review()

    def tearDown(self):
        'called multiple times, once after each test'
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    
    def test__init__id(self):
        'tests __init__: id'
        this_dict = self.new_review.__dict__
        self.assertIsNotNone(this_dict.get("id"))

    def test__init__created_at(self):
        'tests __init__: created_at'
        this_dict = self.new_review.__dict__
        self.assertIsNotNone(this_dict.get("created_at"))

    def test_attributes(self):
        'tests for attributes'
        self.assertTrue(hasattr(self.new_review, "place_id"))
        self.assertEqual(self.new_review.place_id, "")
        self.assertTrue(hasattr(self.new_review, "user_id"))
        self.assertEqual(self.new_review.user_id, "")
        self.assertTrue(hasattr(self.new_review, "text"))
        self.assertEqual(self.new_review.text, "")



        self.assertFalse(hasattr(self.new_review, "updated_at"))
        self.assertFalse(hasattr(self.new_review, "my_number"))
        self.assertFalse(hasattr(self.new_review, "random_attr"))
        self.new_review.name = "TeamTeam!"
        self.new_review.age = 100
        self.assertTrue(hasattr(self.new_review, "name"))
        self.assertEqual(self.new_review.name, "TeamTeam!")
        self.assertTrue(hasattr(self.new_review, "age"))
        delattr(self.new_review, "name")
        self.assertFalse(hasattr(self.new_review, "name"))
        self.assertEqual(self.new_review.__class__.__name__, "BaseModel")

    def test_save_init(self):
        'test to make sure no "updated_at" is created upon creation'
        this_dict = self.new_review.__dict__
        # this_dict = storage.all()
        print("this_dict: {}".format(this_dict))
        self.assertIsNone(this_dict.get("updated_at"))

    def test_save_update(self):
        'tests save: updating a file'
        this_dict = self.new_review.__dict__
        # this_dict = storage.all()
        print("this_dict (before save): {}".format(this_dict))
        before = this_dict.get("updated_at")
        self.new_review.save()
        this_dict = self.new_review.__dict__
        # this_dict = storage.all()
        print("this_dict (after save): {}".format(this_dict))
        after = this_dict.get("updated_at")
        self.assertNotEqual(before, after)
        
    def test___str__(self):
        'test __str__: check format'
        correct_format = ("[{}] ({}) {}".format(self.new_review.__class__.__name__,
                                                self.new_review.id,
                                                self.new_review.__dict__))
        self.assertEqual(print(correct_format), print(self.new_review))

    def test_repr(self):
        str_return = self.new_review.__str__
        self.assertIsNotNone(str_return)

    def test_to_json(self):
        'test to_json'
        json_return = BaseModel.to_json(self.new_review)
        self.assertEqual(type(json_return), dict)

if __name__ == '__main__':
    unittest.main()
