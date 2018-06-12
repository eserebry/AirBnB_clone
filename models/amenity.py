#!/usr/bin/python3
from models.base_model import BaseModel
"""
Class Amenity
"""


class Amenity(BaseModel):
    """
    Class Amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Method initialize
        """
        super().__init__(self, *args, **kwargs)
