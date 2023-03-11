#!/usr/bin/python3
"""
module for State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State model which inherits from BaseModel
    Attributes:
        name: name of the state i.e Lagos.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
