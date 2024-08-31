#!/usr/bin/python3
"""here we have the User class"""
from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
