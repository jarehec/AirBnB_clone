#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


'Module for Review'


class Review(BaseModel):
    'Review class'

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '__init__ method for review'
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
