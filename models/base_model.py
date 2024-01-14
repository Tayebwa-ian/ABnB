#!/usr/bin/python3
"""Base Model - Module
Description:
    It holds common (a union of) characteristics for other models
    Its herited by other model classes in this project
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Holds common model attrs and functions for this project"""

    def __init__(self, *args, **kwargs) -> None:
        """Intializes the class
        Args:
            args: unused arguments
            kwargs: a dictionary of elements used to create
                    object attributes names (only if kwargs is not empty)
        Return: None
        """
        if kwargs:
            for key in kwargs.keys():
                int_attrs = [
                    "number_rooms",
                    "number_bathrooms",
                    "max_guest",
                    "price_by_night"
                ]
                float_attrs = [
                    "longitude",
                    "latitude"
                ]
                if key != "__class__":
                    if key == "created_at":
                        self.created_at = datetime.fromisoformat(kwargs[key])
                    elif key == "updated_at":
                        self.updated_at = datetime.fromisoformat(kwargs[key])
                    elif key == "id":
                        self.id = kwargs[key]
                    elif key in int_attrs:
                        setattr(self, key, int(kwargs[key]))
                    elif key in float_attrs:
                        setattr(self, key, float(kwargs[key]))
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self) -> None:
        """
        Description:
            Update the updated_at field with current date
            and save to JSON file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """
        Description:
            Creates a dictionary containing all keys/values
            of __dict__ of the instance
            This is the first piece
            of the serialization/deserialization process
        Return: dictionary
        """
        dict_obj = {}
        # dict of obj attrs
        self_dict = self.__dict__
        for key in self_dict.keys():
            if key in ["created_at", "updated_at"]:
                dict_obj[key] = datetime.isoformat(self_dict[key])
            else:
                dict_obj[key] = self_dict[key]
        # add key __class__ with the class name of the object
        dict_obj["__class__"] = self.__class__.__name__
        return dict_obj

    def __str__(self) -> str:
        """Return string representation of the object"""
        rep = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return rep
