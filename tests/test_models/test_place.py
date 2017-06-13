#!/usr/bin/python3
"""Unittest for place.py
"""
import unittest
import uuid
import os
import models
from models import storage
from models.place import Plase
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    'class for testing place'

    def setUp(self):
        'called multiple times, once before each test'
        self.new_place = Place()

    def tearDown(self):
        'called multiple times, once after each test'
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test__init__id(self):
        'tests __init__: id'
        this_dict = self.new_place.__dict__
        self.assertIsNotNone(this_dict.get("id"))

    def test__init__created_at(self):
        'tests __init__: created_at'
        this_dict = self.new_place.__dict__
        self.assertIsNotNone(this_dict.get("created_at"))

    def test_attributes(self):
        'tests for attributes'
        self.assertTrue(hasattr(self.new_place, "city_id"))
        self.assertEqual(self.new_place.city_id, "")
        self.assertTrue(hasattr(self.new_place, "user_id"))
        self.assertEqual(self.new_place.user_id, "")
        self.assertTrue(hasattr(self.new_place, "name"))
        self.assertEqual(self.new_place.name, "")
        self.assertTrue(hasattr(self.new_place, "description"))
        self.assertEqual(self.new_place.description, "")
        self.assertTrue(hasattr(self.new_place, "number_rooms"))
        self.assertEqual(self.new_place.number_rooms, 0)
        self.assertTrue(hasattr(self.new_place, "number_bathrooms"))
        self.assertEqual(self.new_place.number_bathrooms, 0)
        self.assertTrue(hasattr(self.new_place, "max_guest"))
        self.assertEqual(self.new_place.max_guest, 0)
        self.assertTrue(hasattr(self.new_place, "price_by_night"))
        self.assertEqual(self.new_place.price_by_night, 0)
        self.assertTrue(hasattr(self.new_place, "latitude"))
        self.assertEqual(self.new_place.latitude, 0.0)
        self.assertTrue(hasattr(self.new_place, "longitude"))
        self.assertEqual(self.new_place.longitude, 0.0)
        self.assertTrue(hasattr(self.new_place, "amenity_ids"))
        self.assertEqual(self.new_place.amenity_ids, [])

        self.assertFalse(hasattr(self.new_place, "updated_at"))
        self.assertFalse(hasattr(self.new_place, "my_number"))
        self.assertFalse(hasattr(self.new_place, "random_attr"))
        self.new_place.name = "TeamTeam!"
        self.new_place.age = 100
        self.assertTrue(hasattr(self.new_place, "name"))
        self.assertEqual(self.new_place.name, "TeamTeam!")
        self.assertTrue(hasattr(self.new_place, "age"))
        delattr(self.new_place, "name")
        self.assertFalse(hasattr(self.new_place, "name"))
        self.assertEqual(self.new_place.__class__.__name__, "BaseModel")

    def test_save_init(self):
        'test to make sure no "updated_at" is created upon creation'
        this_dict = self.new_place.__dict__
        # this_dict = storage.all()
        print("this_dict: {}".format(this_dict))
        self.assertIsNone(this_dict.get("updated_at"))

    def test_save_update(self):
        'tests save: updating a file'
        this_dict = self.new_place.__dict__
        # this_dict = storage.all()
        print("this_dict (before save): {}".format(this_dict))
        before = this_dict.get("updated_at")
        self.new_place.save()
        this_dict = self.new_place.__dict__
        # this_dict = storage.all()
        print("this_dict (after save): {}".format(this_dict))
        after = this_dict.get("updated_at")
        self.assertNotEqual(before, after)

    def test___str__(self):
        'test __str__: check format'
        correct_format = ("[{}] ({}) {}".format
                          (self.new_place.__class__.__name__,
                           self.new_place.id,
                           self.new_place.__dict__))
        self.assertEqual(print(correct_format), print(self.new_place))

    def test_repr(self):
        str_return = self.new_place.__str__
        self.assertIsNotNone(str_return)

    def test_to_json(self):
        'test to_json'
        json_return = BaseModel.to_json(self.new_place)
        self.assertEqual(type(json_return), dict)

if __name__ == '__main__':
    unittest.main()
