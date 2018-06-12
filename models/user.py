#!/usr/bin/python3
from models.base_model import BaseModel
"""
Class User Module
"""


class User(BaseModel):
    """
    Class User
    """
    email = ""
    first_name = ""
    last_name = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """
        Method initialization
        """
        super().__init__(self, *args, **kwargs)
