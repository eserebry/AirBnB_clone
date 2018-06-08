#!/usr/bin/python3
import json
"""
File storage class
"""


class FileStorage:
    """
    Handle storage of files for all classes
    """
    __file_path = "./dev/file.json"
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
        model_id_key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[model_id_key] = obj

    def save(self):
        """
        Method to save __objects to JSON
        """
        file_name = FileStorage.__file_path
        stor_dict = {}
        for model_id, model_obj in FileStorage.__objects.items():
            stor_dict[model_id] = model_obj.to_json(saving_file_storage=True)
        with open(file_name, mode='w') as f:
            json.dump(stor_dict, f)

    def reload(self):
        """
        Method to save JSON into __objects
        """
        file_name = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(file_name. mode='r') as f:
                new_obj = json.load(f)
        except:
            return
        for obj_id, d in new_obj.items():
            key_cls = d['__class__']
            FileStorage.__objects[obj_id] = FileStorage.attr_dict[k_cls](**d)
