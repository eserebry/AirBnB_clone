#!/usr/bin/python3
from models.base_model import BaseModel
from models.state import State
"""
Class City Module
"""


class City(BaseModel):
    """
    Class City
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
        Method initialization
        """
        super().__init__(self, *args, **kwargs)
