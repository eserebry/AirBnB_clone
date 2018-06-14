#!/usr/bin/python3
"""unittests for BaseModel"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class TestBAseModel"""

    def setUp(self):
        """instance setup"""
        self.basemodel = BaseModel()

    def test_init(self):
        self.assertTrue(isinstance(self.basemodel, BaseModel))

    def test_attr(self):
        """Testing the attributes of BaseModel"""
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.assertTrue(hasattr(self.basemodel, "updated_at"))
        self.assertFalse(hasattr(self.basemodel, "random_attr"))
        self.assertFalse(hasattr(self.basemodel, "name"))
        self.basemodel.name = "Betty"
        self.basemodel.age = 89
        self.assertTrue(hasattr(self.basemodel, "name"))
        self.assertEqual(self.basemodel.name, "Betty")
        self.assertTrue(hasattr(self.basemodel, "age"))
        delattr(self.basemodel, "name")
        self.assertFalse(hasattr(self.basemodel, "name"))
        self.assertEqual(self.basemodel.__class__.__name__, "BaseModel")

    def test_method(self):
        """Testing the methods of BaseModel"""
        self.basemodel.save()
        self.assertTrue(hasattr(self.basemodel, "updated_at"))

if __name__ == '__main__':
    unittest.main()
