#!/usr/bin/python3
"""unittests for Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """class TestAmenity"""

    def setUp(self):
        """test setup"""
        self.amenity = Amenity()

    def test_attr(self):
        """Testing the attributes of Amenity"""
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertFalse(hasattr(self.amenity, "random_attr"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")
        self.assertEqual(self.amenity.name, "")

    def test_method(self):
        """Testing the methods of Amenity"""
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_strings(self):
        self.assertEqual(type(self.amenity.name), str)

if __name__ == '__main__':
    unittest.main()
