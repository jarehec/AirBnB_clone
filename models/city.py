#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


'Module for City'


class City(BaseModel):
    'City class'

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        '__init__ method for City'
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
