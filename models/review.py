#!/usr/bin/python3
"""Review Model-Module(Inherits from the BaseModel)"""
from .base_model import BaseModel


class Review(BaseModel):
    """Holds review attributes and Functions
    Attrs:
        text: review message
        user: the user who made the review
        place: the place where it was made
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
