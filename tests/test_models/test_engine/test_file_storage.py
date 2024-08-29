#!/usr/bin/python3
"""testing the FileStorage class"""


import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage_instantation(unittest.TestCase):
    def test_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)
    def test_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage("kdk")
    def test_file_path_is_private(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
    def test__object_is_private(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
    def test_storage_instance(self):
        self.assertIsInstance(models.storage, FileStorage)
