#!/usr/bin/python3
"""City Model-Module(Inherits from the BaseModel)"""
from .base_model import BaseModel


class City(BaseModel):
    """Holds city attributes and Functions
    Attrs:
        name: City's name
        state_id: ID of the state in which the city is
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
