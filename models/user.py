#!/usr/bin/python3
"""User Model-Module(Inherits from the BaseModel)"""
from .base_model import BaseModel


class User(BaseModel):
    """Holds User attributes and Functions
    Attrs:
        email: Person's Email
        password: Person's passward
        first_name: Person's first_name
        last_name: Person's last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
