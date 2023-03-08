#!/usr/bin/python3
"""
module for Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity model.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
