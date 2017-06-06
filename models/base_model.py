#!/usr/bin/python3
import uuid
from datetime import datetime
'Module for BaseModel'


class BaseModel:
    'BaseModel class'
    def __init__(self):
        'initialize data'
        self.id = uuid.uuid1()
        self.created_at = datetime.now()

    def save(self):
        'save method'
        self.updated_at = datetime.now()

    def __str__(self):
        'str method'
        return ("[{}] ({}) {}".format(type(self), self.id, self.__dict__))

    def to_json(self):
        'to json method'
        new_dict = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, uuid.UUID)):
                v = str(v)
            new_dict[k] = (v)
            new_dict['__class__'] = self.__class__.__name__
        return new_dict
