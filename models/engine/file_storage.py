#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary"""
        if cls is not None:
            t_dict = {}
            for key, val in self.__objects.items():
                if cls.__name__ == val.__class__.__name__:
                    t_dict[key] = val
            return t_dict
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it is inside"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del FileStorage.__objects[key]
            self.save()

    def close(self):
        """Method for deserializing the JSON file to obj"""
        self.reload()
