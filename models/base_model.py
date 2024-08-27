#!/usr/bin/python3
"""this is the base class of our project"""


from datetime import datetime
import uuid


class BaseModel:
    """retprsent the base model"""

    def __init__(self, *args, **kwargs):
        args = None
        if kwargs is None or len(kwargs) == 0 :
             self.id = str(uuid.uuid4())
             self.created_at = self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():

                if key == "__class__":
                    continue

                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)

                setattr(self, key, value)

    def __str__(self):
        """ return the class name and the its id with attributes"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """update the update_at attribute when the instance is changed"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictinary containing all key/value in the __dict__
        of the i'name': 'My First Model'nstance"""
        instance = self.__dict__
        instance["created_at"] = self.created_at.isoformat()
        instance["updated_at"] = self.updated_at.isoformat()
        instance["__class__"] = type(self).__name__

        return instance
