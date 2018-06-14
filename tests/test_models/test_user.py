#!/usr/bin/python3
"""unittests for User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """class TestUser"""
    def test_user(self):
        """testing for a type of the attributes and
        if attributes are not empty"""
        user = User()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime.datetime)
        self.assertIsInstance(user.updated_at, datetime.datetime)
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.first_name)
        self.assertIsNotNone(user.last_name)
        self.assertIsNotNone(user.password)

if __name__ == '__main__':
    unittest.main()