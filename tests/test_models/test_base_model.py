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
        self.assertTrue(isinstance(self.base12, BaseModel))

    def testattr(self):
        """Testing the attributes of BaseModel"""
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.assertFalse(hasattr(self.basemodel, "updated_at"))
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

    def testmethod(self):
        """Testing the methods of BaseModel"""
        self.basemodel.save()
        self.assertTrue(hasattr(self.basemodel, "updated_at"))

    def teststr(self):
        """Testing the str format of BaseModel"""
        s = "[{}] ({}) {}".format(self.basemodel.__class__.__name__,
                                  str(self.basemodel.id),
                                  self.basemodel.__dict__)
        self.assertEqual(print(s), print(self.basemodel))

if __name__ == '__main__':
    unittest.main()
