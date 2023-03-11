#!/usr/bin/python3
"""
contains test module for City class.
"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    """
    defines module to testing City class.
    """

    def test_pep8_model(self):
        """
            Tests for pep8 model
        """
        files = []
        files.append('tests/test_models/test_city.py')
        files.append('models/city.py')
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(files)
        self.assertEqual(p.total_errors, 0, "pep8 error")

    def test_city(self):
        """
        test for city instance
        """
        city0 = City()
        self.assertIsInstance(city0, BaseModel)

    def test_attribute(self):
        """
        test for city attributes:
        attribute:
            name: city name
            state_id: state identifier for the city
        """
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

    def test_compare_cities(self):
        """
        test to compare cities
        """
        state = State()
        state.name = "Lagos"
        city0 = City()
        city0.name = "Maryland"
        city0.state_id = state.id
        
        city1 = City()
        city1.name = "Lagos Mainland"
        city1.state_id = state.id

        self.assertNotEqual(city0, city1)
        self.assertNotEqual(city0.id, city1.id)
        self.assertNotEqual(city0.name, city1.name)
        self.assertEqual(city0.state_id, city1.state_id)
