#!/usr/bin/python3
""" defines all common attributes/methods for other classes """
import uuid
import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """ Initialise class BaseMode
        Args:
            id (str): uuid
            created_at (int): datetimr
            updated_at (int): datetime
        """
        self.id = None
        self.created_at = None
        self.updated_at = None

    def id(self):
        """assign with an uuid when an instance is created"""
        id = uuid.uuid4()
        return str(self.id)

    def created_at(self):
        """assign with the current datetime when an instance is created"""
        return self.created_at

    def updated_at(self):
        """ assign with the current datetime when an instance is created"""
        return self.updated_at

    def save(self):
        """updates the public attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

    def __str__(self):
        """returns string with the BaseModel arguments"""
        return "[BaseModel] (%s) %s" % \
            (self.id, self.__dict__)
