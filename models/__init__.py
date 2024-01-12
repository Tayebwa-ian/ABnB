#!/usr/bin/python3
"""create a unique FileStorage instance for the application"""
from .engine import file_storage
from .base_model import BaseModel
from .amenity import Amenity
from .city import City
from .place import Place
from .review import Review
from .state import State
from .user import User


storage = file_storage.FileStorage()
storage.reload()
