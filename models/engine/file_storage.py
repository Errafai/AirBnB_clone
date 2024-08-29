#!/usr/bin/python3
"""this moudle define the FileStorage class"""


from models.base_model import BaseModel
import json


class FileStorage:
    """represent the FileStorage class:
    Attrs:
        file_path (str): a private class attr that hold
                         the json file
        objects (dict): a dictionary that holds a BaseModle objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """get the objects attribute"""
        return self.__objects

    def new(self, obj):
        """add the new obj to the objects dict"""
        obj_id = obj.__class__.__name__ + "." + obj.id
        self.__objects[obj_id] = obj

    def save(self):
        """serializes objects to the JSON file"""
        cls_objs = self.__objects
        objs_to_dict = {ob: cls_objs[ob].to_dict() for ob in cls_objs.keys()}
        with open(self.__file_path, "w") as jfile:
            json.dump(objs_to_dict, jfile)

    def reload(self):
        """deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, "r") as jfile:
                inst_objs = json.load(jfile)
                for value in inst_objs.values():
                    cls_obj = value["__class__"]
                    del value["__class__"]
                    new_obj = eval(cls_obj)(**value)
                    self.new(new_obj)

        except FileNotFoundError:
            pass
