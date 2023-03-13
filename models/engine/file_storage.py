#!/usr/bin/python3
"""
Module file_storage serializes instances to a JSON
file and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    custom class for file storage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns a dictionary representation of all objects.
        """
        return self.__objects

    def new(self, object):
        """
        sets object in __objects using the key
        <object class name>.id

        Args:
            object: object to write
        """
        self.__objects[
            object.__class__.__name__ + "." +
            str(object.id)
        ] = object

    def save(self, obj=None):
        """
        serializes __object to a JSON file
        (file path: __file_path)
        """
        with open(self.__file_path, "w+") as fp:
            json.dump(
                {
                    key: value.to_dict()
                    for key, value in self.__objects.items()
                }, fp
            )

    def reload(self):
        """
         deserializes the JSON file to __objects if it exists
        """
        try:
            with open(self.__file_path, "r") as fp:
                data = json.loads(fp.read())
                for value in data.values():
                    cls = value.get('__class__')
                    if cls:
                        obj = eval(cls)(**value)
                        self.new(obj)
        except Exception:
            pass
