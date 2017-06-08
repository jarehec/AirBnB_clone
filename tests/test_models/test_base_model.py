#!/usr/bin/python3
"""Unittest for base_model.py
"""
import unittest
import uuid
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    'class for testing base_model'
    def test_name(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        self.assertEqual(my_model.name, "Holberton")

    def test_no_name(self):
        my_model = BaseModel()
        with self.assertRaises(AttributeError):
            my_model.name

    def test_no_id(self):
        my_model = BaseModel()
        my_model.id

    def test_no_number(self):
        my_model = BaseModel()
        with self.assertRaises(AttributeError):
            my_model.my_number

    def test_check_id_type(self):
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model.id, uuid.UUID))

    def test_save(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()

    def test_save_str(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        with self.assertRaises(TypeError):
            my_model.save("hi")

    def test_save_int(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        with self.assertRaises(TypeError):
            my_model.save(42)

    def test_save_tuple(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        with self.assertRaises(TypeError):
            my_model.save((42, 98))

    def test_save_list(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        with self.assertRaises(TypeError):
            my_model.save([42, 98])

    def test_save_set(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        with self.assertRaises(TypeError):
            my_model.save({'42', '98'})

    def test_save_dict(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        with self.assertRaises(TypeError):
            my_model.save({'42': '98'})

    def test_to_json(self):
        my_model = BaseModel()
        my_model_json = my_model.to_json()

    def test_to_json_str(self):
        my_model = BaseModel()
        with self.assertRaises(TypeError):
            my_model_json = my_model.to_json('3')

    def test_to_json_int(self):
        my_model = BaseModel()
        with self.assertRaises(TypeError):
            my_model_json = my_model.to_json(3)

    def test_to_json_set(self):
        my_model = BaseModel()
        with self.assertRaises(TypeError):
            my_model_json = my_model.to_json({'t', '3'})

    def test_to_json_dict(self):
        my_model = BaseModel()
        with self.assertRaises(TypeError):
            my_model_json = my_model.to_json({'ti': '3'})

    def test_to_json_list(self):
        my_model = BaseModel()
        with self.assertRaises(TypeError):
            my_model_json = my_model.to_json(['ti', '3'])

    def test_to_json_tuple(self):
        my_model = BaseModel()
        with self.assertRaises(TypeError):
            my_model_json = my_model.to_json(('ti', '3'))

    def test_datetime(self):
        my_model = BaseModel()
        
if __name__ == '__main__':
    unittest.main()
