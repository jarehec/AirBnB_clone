#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


'Module for Place'


class Place(BaseModel):
    'Place class'

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        '__init__ method for place'
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
