# !/usr/bin/python3
"""testing the base_model class"""


import unittest
import os
import sys
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def setUp(self):
        """setUp two instances"""

        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_uuid(self):
        self.assertIsInstance(self.b1, BaseModel)
        self.assertTrue(hasattr(self.b1, "id"))
        self.assertIsInstance(self.b1.id, str)

        self.assertIsInstance(self.b2, BaseModel)
        self.assertTrue(hasattr(self.b2, "id"))
        self.assertIsInstance(self.b2.id, str)

        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_created_at_attribute(self):
        self.assertTrue(hasattr(self.b1, "created_at"))
        self.assertTrue(hasattr(self.b2, "created_at"))

        self.assertNotEqual(self.b1.created_at, datetime.now())
        self.assertNotEqual(self.b2.created_at, datetime.now())

        self.assertNotEqual(self.b1.created_at, self.b2.created_at)

    def test_updated_at_attribute(self):
        self.assertTrue(hasattr(self.b1, "updated_at"))
        self.assertTrue(hasattr(self.b2, "updated_at"))

        self.assertNotEqual(self.b1.updated_at, datetime.now())
        self.assertNotEqual(self.b2.updated_at, datetime.now())

        self.assertEqual(self.b1.updated_at, self.b1.created_at)
        self.assertEqual(self.b2.updated_at, self.b2.created_at)

        self.assertNotEqual(self.b1.updated_at, self.b2.created_at)

    def test_the__str__method(self):
        dt = datetime.today()
        self.b1.id = '123930'
        self.b1.created_at = self.b1.updated_at = dt
        bstr = self.b1.__str__()
        self.assertIn("[BaseModel] (123930)", bstr)
        self.assertIn("'id': '123930'", bstr)
        self.assertIn("'created_at': " + repr(dt), bstr)
        self.assertIn("'updated_at': " + repr(dt), bstr)

    def tearDown(self):
        self.b1 = None
        self.b2 = None

class TestBaseModel_save(unittest.TestCase):
    """testing the save method"""

    def setUp(self):
        """declaring an instance"""
        self.b = BaseModel()

    def test_updated_at_changed(self):
        self.b.name = "testing"
        old_update = self.b.updated_at
        self.b.save()
        self.assertNotEqual(old_update,  self.b.updated_at)

    def test_updated_at_vs_creadted_at(self):
        self.b.number = 39
        self.b.save()
        self.assertNotEqual(self.b.created_at,  self.b.updated_at)

class TestBaseModel_to_dict(unittest.TestCase):
    """testing the `to_dict()` method"""

    def setUp(self):
        """declaring an instance"""
        self.b = BaseModel()

    def test_it_return_a_dict(self):
        """checking if the returnr of the method is a dict"""
        self.assertIsInstance(self.b.to_dict(), dict)

    def test_attributes_in_dict(self):
        """testing some attributes if they exist in the dict"""
        dict_attr = self.b.to_dict()
        self.assertIn("__class__", dict_attr)
        self.assertIn("created_at", dict_attr)
        self.assertIn("updated_at", dict_attr)
        self.assertIn("id", dict_attr)

    def test_example_of_dict(self):
        self.b.name = "My First Model"
        self.b.my_number = 89
        self.b.save()
        dict_attr = self.b.to_dict()
        self.assertIn("my_number", dict_attr)
        self.assertEqual(dict_attr["my_number"], 89)
        self.assertIn("name", dict_attr)
        self.assertIn(dict_attr["name"], "My First Model")

    def test_isofomat_of_time(self):
        """checking if the `created_at` and `updated_at` attr
        are in isofomat inside the dict"""
        dict_attr = self.b.to_dict().copy()
        created = dict_attr["created_at"]
        self.b.save()
        updated = dict_attr["updated_at"]

        self.assertIsInstance(created, str)
        self.assertIsInstance(updated, str)
        self.assertRegex(created, r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(.\d+)?$')
        self.assertRegex(updated, r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(.\d+)?$')



if __name__ == '__main__':
    unittest.main()
