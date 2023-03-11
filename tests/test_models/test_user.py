#!/usr/bin/python3
"""
Test for User model
"""

import unittest
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    def test_pep8_model(self):
        """
            Tests for pep8 model
        """
        files = []
        files.append('tests/test_models/test_user.py')
        files.append('models/user.py')
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(files)
        self.assertEqual(p.total_errors, 0, "pep8 error")
    
    def test_user(self):
        """
        test user
        """
        user0 = User()
        self.assertIsInstance(user0, BaseModel)

    def test_attributes(self):
        """
        test attributes
        """
        user0 = User()
        self.assertTrue(hasattr(user0, "first_name"))
        self.assertTrue(hasattr(user0, "last_name"))
        self.assertTrue(hasattr(user0, "email"))
        self.assertTrue(hasattr(user0, "password"))
        self.assertEqual(user0.email, "")
