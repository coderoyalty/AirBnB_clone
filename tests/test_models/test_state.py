#!/usr/bin/python3
"""
Contains test module for State class
"""
import unittest
import pep8
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_pep8_model(self):
        """
            Tests for pep8 model
        """
        files = []
        files.append('tests/test_models/test_state.py')
        files.append('models/state.py')
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(files)
        self.assertEqual(p.total_errors, 0, "pep8 error")

    def test_attributes(self):
        """
        test for State attributes
        attributes:
            name: a state attribute for the state name
            id: identifier for the state
        """
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "name"))

    def test_state(self):
        """
        test for state as an instance of BaseModel
        """
        state0 = State()
        self.assertIsInstance(state0, BaseModel)
