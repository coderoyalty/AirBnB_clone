#!/usr/bin/python3
"""
contains the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class that represents a User

    attributes:
        email: string
        password: string
        first_name: string
        last_name: string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
