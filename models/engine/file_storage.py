#!/usr/bin/python3
import uuid
import json

'File storage module'


class FileStorage:
    'FileStorage class'
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        'Returns __objects'
        return self.reload()

    def new(self, obj):
        'adds an object to the instance'
        from models.base_model import BaseModel
        import uuid

        class_name = str(obj.__class__.__name__)
        obj_id = str(obj.id)
        obj_str = class_name + "." + obj_id
        FileStorage.__objects[obj_str] = obj

    def save(self):
        'serializes __objects to JSON file'
        from models.base_model import BaseModel
        new_dict = {}

        for keys in FileStorage.__objects.keys():
            new_dict[keys] = (FileStorage.__objects[keys]).to_json()

        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        'deserializes the JSON file to __objects'
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review
    
        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}
        try:
            with open(FileStorage.__file_path,
                      mode="r", encoding="utf-8") as f:
                reloaded = json.load(f)
                for k, v in reloaded.items():
                    class_n = classes.get(reloaded[k].get('__class__'))
                    self.__objects[k] = class_n(**reloaded[k])
                return self.__objects
        except:
            return {}
