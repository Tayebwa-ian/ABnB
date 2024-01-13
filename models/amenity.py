#!/usr/bin/python3
"""Amenity Model-Module(Inherits from the BaseModel)"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """Holds amenity attributes and Functions
    Attrs:
        name: Amenity's name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
