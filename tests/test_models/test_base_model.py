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
        # self.assertIsInstance(self.b1, datetime)

        self.assertTrue(hasattr(self.b2, "created_at"))
        # self.assertIsInstance(self.b2.created_at, datetime)

        self.assertNotEqual(self.b1.created_at, datetime.now())
        self.assertNotEqual(self.b2.created_at, datetime.now())

        self.assertNotEqual(self.b1.created_at, self.b2.created_at)

    def test_updated_at_attribute(self):
        self.assertTrue(hasattr(self.b1, "updated_at"))
        # self.assertIsInstance(self.b1, datetime)

        self.assertTrue(hasattr(self.b2, "updated_at"))
        # self.assertIsInstance(self.b2.updated_at, datetime)

        self.assertNotEqual(self.b1.updated_at, datetime.now())
        self.assertNotEqual(self.b2.updated_at, datetime.now())

        # self.assertEqual(self.b1.updated_at, self.b1.created_at)
        # self.assertEqual(self.b2.updated_at, self.b2.created_at)

        self.assertNotEqual(self.b1.updated_at, self.b2.created_at)

    def tearDown(self):
        self.b1 = None
        self.b2 = None

class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

if __name__ == '__main__':
    unittest.main()
