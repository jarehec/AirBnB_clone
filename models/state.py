#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


'Module for State'


class State(BaseModel):
    'State class'

    name = ""

    def __init__(self, *args, **kwargs):
        '__init__ method for State'
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
