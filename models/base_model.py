#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

'Module for BaseModel'


class BaseModel:
    'BaseModel class'
    def __init__(self, *args, **kwargs):
        'initialize data'
        if len(kwargs) is not 0:
            self.id = kwargs.get("id")
            self.created_at = datetime(kwargs.get("created_at"))
            self.updated_at = datetime(kwargs.get("updated_at"))
        else:
            self.id = str(uuid.uuid1())
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        'save method'
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        'str method'
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def to_json(self):
        'to json method'
        new_dict = {}
        if type(self) is not dict:
            for k, v in self.__dict__.items():
                if isinstance(v, (datetime, uuid.UUID, list, set)):
                    v = str(v)
                new_dict[k] = (v)
        else:
            for k1, v1 in self.items():
                if isinstance(v1, (datetime, uuid.UUID, dict, list, set)):
                    v1 = str(v1)
                new_dict[k1] = (v1)
                
        new_dict['__class__'] = str(self.__class__.__name__)
        return new_dict
