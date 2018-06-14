#!/usr/bin/python3
import uuid
from datetime import datetime
import models
""" defines all common attributes/methods for other classes """
"""module: base_model"""

"""
Base class for all models will contain id, created_at
and updated at attributes. Save() and to_json() methods
"""


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ Initialise class BaseMode
        Args:
        *args - not used
        **kwargs - dictionary, contains arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """updates the public attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """returns string with the BaseModel arguments"""
        return ("[{}] ({}) {}".format(self..__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
        Method returns official repreentations
        of string
        """
        cls = self.__class__.__name__
        string = ("[{}] ({}) {}".format(cls, self.id, self.__dict__))
        return (string)

    def to_dict(self):
        """
        Method to return a dict containing all key/value of __dict__
        instance
        """
        my_dict = dict(**self.__dict__)
        my_dict['__class__'] = str(type(self).__name__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
