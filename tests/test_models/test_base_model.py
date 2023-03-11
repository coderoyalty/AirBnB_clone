#!/usr/bin/python3
"""
Test for base model
"""

import unittest
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """
        Test Model for testing attributes of base model
    """

    def test_pep8_model(self):
        """
            Tests for pep8 model in specific files
        """
        files = []
        files.append('models/base_model.py')
        files.append('tests/test_models/test_base_model.py')
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(files)
        self.assertEqual(p.total_errors, 0, "pep8 error")

    def test_uuid(self):
        """
        universal unique identifier
        """
        model0 = BaseModel()
        model1 = BaseModel()
        self.assertTrue(hasattr(model0, "id"))
        self.assertTrue(hasattr(model1, "id"))
        self.assertNotEqual(model0.id, model1.id)
        self.assertIsInstance(model0, BaseModel)
        self.assertIsInstance(model0.id, str)

    def test_basic(self):
        """
            test inputs for the BaseModel class
        """
        model = BaseModel()
        model.name = "BaseModel"
        model.percent = 90

        self.assertEqual(
            [model.name, model.percent],
            ["BaseModel", 90]
        )
        self.assertTrue(hasattr(model, "name"))
        self.assertTrue(hasattr(model, "percent"))

    def test_attributes(self):
        """
            Test id attribute of the model
        """
        model0 = BaseModel()
        model1 = BaseModel()
        model0_dict = model0.to_dict()
        model1_dict = model1.to_dict()
        c_model0 = BaseModel(**model0_dict)
        c_model0_dict = c_model0.to_dict()

        self.assertNotEqual(
            model0_dict, model1_dict
        )
        self.assertEqual(
            model0_dict, c_model0_dict
        )
