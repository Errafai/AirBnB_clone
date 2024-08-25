#!/usr/bin/python3
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
        #self.assertIsInstance(self.b1, datetime)

        self.assertTrue(hasattr(self.b2, "created_at"))
        #self.assertIsInstance(self.b2.created_at, datetime)

        self.assertNotEqual(self.b1.created_at, datetime.now())
        self.assertNotEqual(self.b2.created_at, datetime.now())

        self.assertNotEqual(self.b1.created_at, self.b2.created_at)

    def test_updated_at_attribute(self):
        self.assertTrue(hasattr(self.b1, "updated_at"))
        #self.assertIsInstance(self.b1, datetime)

        self.assertTrue(hasattr(self.b2, "updated_at"))
        #self.assertIsInstance(self.b2.updated_at, datetime)

        self.assertNotEqual(self.b1.updated_at, datetime.now())
        self.assertNotEqual(self.b2.updated_at, datetime.now())

        #self.assertEqual(self.b1.updated_at, self.b1.created_at)
        #self.assertEqual(self.b2.updated_at, self.b2.created_at)

        self.assertNotEqual(self.b1.updated_at, self.b2.created_at)

    def tearDown(self):
        self.b1 = None
        self.b2 = None


if __name__ == '__main__':
    unittest.main()
