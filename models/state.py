#!/usr/bin/python3
"""
module for State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State model.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
