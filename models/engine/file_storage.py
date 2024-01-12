#!/usr/bin/python3
"""
File storage Module
Serialization and Deserialization of JSON data to and from a file
"""
import json
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State
from ..user import User


class FileStorage:
    """
    Description:
        serializes instances to a JSON file
        And deserializes JSON file to instances
    Attrs:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects
                    by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """return a dictionary object of __objects"""
        return self.__objects

    def new(self, obj) -> None:
        """sets in __objects the obj with key <obj class name>.id
        Agrs:
            obj: the object of a class passed
        Return: None
        """
        key = obj.__class__.__name__ + ".{}".format(obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self) -> None:
        """ serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file, indent="\t")

    def reload(self) -> None:
        """
        Description:
            Deserializes the JSON file to __objects
            only if the JSON file (__file_path) exists ; otherwise, do nothing.
            If the file does not exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
