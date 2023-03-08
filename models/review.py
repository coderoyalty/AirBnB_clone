#!/usr/bin/python3
"""
module for Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class
    """
    user_id = ""
    place_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
