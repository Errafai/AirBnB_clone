#!/usr/bin/python3
"""this is the base class of our project"""


from datetime import datetime
import uuid


class BaseModel:
    """retprsent the base model"""

    def __init__(self):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ return the class name and the its id with attributes"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__class__)

    def save(self):
        """update the update_at attribute when the instance is changed"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictinary containing all key/value in the __dict__
        of the instance"""
        instance = self.__dict__
        instance["created_at"] = self.created_at.isoformat()
        instance["updated_at"] = self.updated_at.isoformat()
        instance["__class__"] = type(self).__name__

        return instance
