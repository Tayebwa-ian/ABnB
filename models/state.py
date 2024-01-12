#!/usr/bin/python3
"""State Model-Module(Inherits from the BaseModel)"""
from .base_model import BaseModel


class State(BaseModel):
    """Holds state attributes and Functions
    Attrs:
        name: State's name
    """
    name = ""
