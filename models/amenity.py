#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
from models.base_mode import BaseModel


'Module for Amenity'


class Amenity(BaseModel):
    'Amenity class'

    name = ""

    def __init__(self, *args, **kwargs):
        '__init__ method for amenity'
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
