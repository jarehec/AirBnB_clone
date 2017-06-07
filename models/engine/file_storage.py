#!/usr/bin/python3
import uuid
import json
'File storage module'

class FileStorage:
    'FileStorage class'
    def __init__(self):
        'Initialize data'
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        'Returns __objects'
        return self.__objects

    def new(self, obj):
        'adds an object to the instance'
        class_name = self.__class__.__name__
        obj_id = uuid.uuid1()
        self.__objects[class_name.obj_id] = obj

    def save(self):
        'serializes __objects to json file'
        with open(self.__file_path, "r", "utf-8") as f:
            json.dumps(self.__objects, f)

    def reload(self):
        'deserializes the JSON file to __objects'
