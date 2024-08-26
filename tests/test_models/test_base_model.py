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




if __name__ == '__main__':
    unittest.main()
