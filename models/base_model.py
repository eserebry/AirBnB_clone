#!/usr/bin/python3
""" defines all common attributes/methods for other classes """
import uuid
import datetime
import json


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """ Initialise class BaseMode
        Args:
            id (str): uuid
            created_at (int): datetime
            updated_at (int): datetime
        """
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now())
        self.updated_at = str(datetime.datetime.now())

    def save(self):
        """updates the public attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at
        my_dict['id'] = self.id
        my_dict['updated_at'] = self.updated_at
        return my_dict

    def __str__(self):
        """returns string with the BaseModel arguments"""
        return "[%s] (%s) %s" % \
            (self.__class__.__name__, self.id, self.__dict__)
