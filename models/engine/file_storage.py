#!/usr/bin/python3
import uuid
import json

'File storage module'


class FileStorage:
    'FileStorage class'
    print("++FileStorage++")
    __file_path = "./file.json"
    __objects = {}
        
    def all(self):
        'Returns __objects'
        print("++FileStorage.all++")
        return self.reload()

    def new(self, obj):
        'adds an object to the instance'
        print("++FileStorage.new++")
        from models.base_model import BaseModel
        import uuid

        class_name = str(obj.__class__.__name__)
        obj_id = str(obj.id)
        obj_str = class_name + "." + obj_id
        FileStorage.__objects[obj_str] = obj

    def save(self):
        'serializes __objects to JSON file'
        print("++FileStorage.save++")
        from models.base_model import BaseModel
        new_dict = {}

        for keys in FileStorage.__objects.keys():
            new_dict[keys] = (FileStorage.__objects.get[keys]).to_json()

        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        'deserializes the JSON file to __objects'
        print("++FileStorage.reload++")
        from models.base_model import BaseModel
        print("above try")
        # try:
        print("__file_path: {}".format(self.__file_path))
        print("in try")
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                print("file has been opened")
                reloaded = json.load(f)
                print("successful reload. reloaded: {} ".format(reloaded))
                for k in reloaded.keys():
                    self.__objects[k] = BaseModel(**reloaded[k])
                print(self.__objects)
                return self.__objects
        except:
            return {}
