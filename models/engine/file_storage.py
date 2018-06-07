#!/usr/bin/python3
import json
"""
File storage class
"""



class FileStorage:
    """
    Handle storage of files for all classes
    """
    __file_path ="./dev/file.json"
    __objects = {}

    attr_dict = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity
        'City': city.City
        'State': state.State
        'Place': place.Place
        'Review': review.Review
        'User': user.User
    def all(self, cls=None):
        """
        Method return __objects
        """
        if cls is not None:
            new_obj = {}
            for cls_id, obj, in FileStorage.__objects.items():
                if type(obj).__name__ = obj
            return new_obj
        else:
            return FileStorage.__objects

    def new(self, obj):
        """
        Method sets obj in dictionary with id as key
        """
        model_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[model_id] = obj

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
