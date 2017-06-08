#!/usr/bin/python3
'Unittest for FileStorage class'
import unittest
import uuid
import json
import models.engine.file_storage

FileStorage = models.engine.file_storage.FileStorage
all = FileStorage.all
new = FileStorage.new
save = __import__('file_storage').save
reload = __import__('file_storage').reload

class TestFileStorageDocs(unittest.Testcase):
    'Tests for docs for FileStorage class'
    def test_doc_file(self):
        'Test: file documentation'
        expected: 'File storage module'
        actual: models.file_storage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        'Test: class documentation'
        expected: 'FileStorage class'
        actual: FileStorage.__doc__
        self.assertEqual(expected, actual)

    def test_dic_method_all(self):
        'Test: method (all) documentation'
        expected: 'Returns __objects'
        actual: FileStorage.all.__doc__
        self.assertEqual(expected, actual)

    def test_dic_method_new(self):
        'Test: method (new) documentation'
        expected: 'adds an objects to the instance'
        actual: FileStorage.new.__doc__
        self.assertEqual(expected, actual)

    def test_dic_method_save(self):
        'Test: method (save) documentation'
        expected: 'serializes __objects to JSON file'
        actual: FileStorage.save.__doc__
        self.assertEqual(expected, actual)

    def test_dic_method_reload(self):
        'Test: method (reload) documentation'
        expected: 'deserializes the JSON file to __objects'
        actual: FileStorage.reload.__doc__
        self.assertEqual(expected, actual)


@classmethod
def setUpClass(cls):
    'Sets up __file_path and __objects for tests'
    __file_path = "./file.json"
    __objects = {}
    

class TestAll(unittest.TestCase):
    'Tests all method from FileStorage'
    def test_empty__object(self):
        'all test: __object is an empty dictionary'
        self.assert___(all(),)

class TestNew(unittest.TestCase):
    'Tests new method from FileStorage'


class TestSave(unittest.TestCase):
    'Tests save method from FileStorage'

class TestReload(unittest.TestCase):
    'Tests reload method from FileStorage'


if __name__ == '__main__':
    unittest.main()
