#!/usr/bin/python3
"""here we have the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
