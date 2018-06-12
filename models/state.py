#!/usr/bin/python3
from models.base_model import BaseModel
"""
Class State Module
"""


class State(BaseModel):
    """
    Class State
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Method initialization
        """
        super().__init__(self, *args, **kwargs)
