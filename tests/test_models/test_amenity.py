#!/usr/bin/python3
"""
Test for Amenity model
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    def test_pep8_model(self):
        """
            Tests for pep8 model
        """
        files = []
        files.append('tests/test_models/test_amenity.py')
        files.append('models/amenity.py')
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(files)
        self.assertEqual(p.total_errors, 0, "pep8 error")

    def test_amenity(self):
        """
        test amenity
        """
        amenity0 = Amenity()
        self.assertIsInstance(amenity0, BaseModel)

    def test_attributes(self):
        """
        test attributes
        """
        amenity0 = Amenity()
        self.assertTrue(hasattr(amenity0, "name"))
