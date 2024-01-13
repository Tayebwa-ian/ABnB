#!/usr/bin/python3
"""Place Model-Module(Inherits from the BaseModel)"""
from .base_model import BaseModel


class Place(BaseModel):
    """Holds place attributes and Functions
    Attrs:
        city_id: city id of the place
        user_id: User id of person in the place
        name: the name of the place
        description: Brief decription of the place
        number_rooms: room number
        number_bathrooms: number of bathrooms in the room
        max_guest: maximum guest the room can host
        price_by_night: price charged per night
        latitude: latitude coordinates
        longitude: longitude coordinates
    """
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

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
