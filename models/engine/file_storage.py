#!/usr/bin/python3
"""this moudle define the FileStorage class"""


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
        obj_dict = obj.to_dict()
        print(obj_dict)

        self.__objects[obj_id] = obj_dict

    def save(self):
        """serializes objects to the JSON file"""
        with open(self.__file_path, "w") as jfile:
            json.dump(self.__objects, jfile)

    def reload(self):
        """deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, "r") as jfile:
                try:
                    self.__objects = json.load(jfile)
                except Exception:
                    pass
        except FileNotFoundError:
            pass


