#!/usr/bin/python3
"""
Contains test module for Place class
"""
import unittest
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def test_pep8_model(self):
        """
            Tests for pep8 model
        """
        files = []
        files.append('tests/test_models/test_place.py')
        files.append('models/place.py')
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(files)
        self.assertEqual(p.total_errors, 0, "pep8 error")

    def test_attributes(self):
        """
        test for Place attributes
        attributes:
            name: a place attribute for the place name
            id: identifier for the place
        """
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))

    def test_type_attributes(self):
        """
        test for type of Place attributes
        """
        place = Place()
        self.assertTrue(type(0), type(place.id))
        self.assertTrue(type(""), type(place.name))
        self.assertTrue(type(""), type(place.city_id))
        self.assertTrue(type(""), type(place.user_id))
        self.assertTrue(type(""), type(place.description))
        self.assertTrue(type(0.0), type(place.latitude))
        self.assertTrue(type(0.0), type(place.longitude))
        self.assertTrue(type([]), type(place.amenity_ids))
        self.assertTrue(type(0), type(place.price_by_night))
        self.assertTrue(type(0), type(place.max_guest))
        self.assertTrue(type(0), type(place.number_rooms))
        self.assertTrue(type(0), type(place.number_bathrooms))
