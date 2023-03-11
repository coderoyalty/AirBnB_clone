#!/usr/bin/python3
"""
Contains test module for Review class
"""

import unittest
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def test_pep8_model(self):
        """
            Tests for pep8 model
        """
        files = []
        files.append('tests/test_models/test_review.py')
        files.append('models/review.py')
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(files)
        self.assertEqual(p.total_errors, 0, "pep8 error")

    def test_attributes(self):
        """
        test for Review attributes
        attributes:
            name: a review attribute for the review name
            id: identifier for the review
        """
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_review(self):
        """
        test for review as an instance of BaseModel
        """
        review0 = Review()
        self.assertIsInstance(review0, BaseModel)

    def test_type_attribute(self):
        """
        test for type of review attributes
        """
        review = Review()
        self.assertTrue(type(review.place_id), type(""))
        self.assertTrue(type(review.user_id), type(""))
        self.assertTrue(type(review.text), type(""))
