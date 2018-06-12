#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User
"""
Class Review Module
"""


class Review(BaseModel):
    """
    Class Review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Method initialization
        """
        super().__init__(self, *args, **kwargs)
