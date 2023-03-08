#!/usr/bin/python3
"""
module for City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City model.
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
