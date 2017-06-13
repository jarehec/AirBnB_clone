#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
#does BaseModel need to be imported?

'Module for User'


class User(BaseModel):
    'User class'

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '__init__ method for user'
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
