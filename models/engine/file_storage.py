#!/usr/bin/python3
import os.path
import json
"""
File storage class
"""


class FileStorage:
    """
    Handle storage of files for all classes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method return all instances of obj
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Method sets obj in dictionary with id as key
        """
        model_id_key = str(obj.__class__.__name__) + '.' + str(obj.id)
        self.__objects[model_id_key] = obj

    def save(self):
        """
        Method to save __objects to JSON
        """
        stor_dict = {}
        for i, obj in self.__objects.items():
            stor_dict[i] = obj.to_dict()
        with open(self.__file_path, 'w+') as f:
            json.dump(stor_dict, f)

    def reload(self):
        """method: reload - deserialize"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                read = json.load(f)
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.place import Place
            from models.amenity import Amenity
            from models.review import Review
            for i in read.keys():
                if read[i]["__class__"] == "BaseModel":
                    self.__objects[i] = BaseModel(**read[i])
                elif read[i]["__class__"] == "User":
                    self.__objects[i] = User(**read[i])
                elif read[i]["__class__"] == "State":
                    self.__objects[i] = State(**read[i])
                elif read[i]["__class__"] == "City":
                    self.__objects[i] = City(**read[i])
                elif read[i]["__class__"] == "Place":
                    self.__objects[i] = Place(**read[i])
                elif read[i]["__class__"] == "Amenity":
                    self.__objects[i] = Amenity(**read[i])
                elif read[i]["__class__"] == "Review":
                    self.__objects[i] = Review(**read[i])
            return self.__objects
        else:
            return {}
