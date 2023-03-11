#!/usr/bin/python3
"""
    defines the BaseModel class for the entire project.
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
        base for all the classes in the airBnB project

        Attributes:
            id (string): assign with an uuid when instance is created
            created_at: assign with the current datetime when an
            instance is created
            updated_at: update every time you change your object
        Methods:
            __str__: print class name, id, and creates dictionary
            save: updates the public instance attribute updated_at
            with the current datetime.
            to_dict: returns a dictionary containing all keys/values
            of __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """
        public instance initialization after creation.
        Args:
            *args(args): arguments
            **kwargs(dict): attribute values
        """
        FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, FORMAT)
                elif key == 'id':
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def save(self):
        """
            Updates the public instance attribute update_at with
            the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values of __dict__
            of the instance.
        """

        objects = self.__dict__.copy()
        objects["updated_at"] = self.updated_at.isoformat()
        objects["created_at"] = self.created_at.isoformat()
        objects['__class__'] = self.__class__.__name__
        return objects

    def __str__(self):
        """
        print class name, id, dictionary
        """

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )
