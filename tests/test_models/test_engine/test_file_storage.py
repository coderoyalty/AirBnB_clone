#!/usr/bin/python3
"""
Unittest for file storage
"""
import unittest
import pep8
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    test attributes of FileStorage
    """

    def setup(self):
        """
        classes needed testing
        """
        pass

    def test_pep8_model(self):
        """
            run pep8 tests for files
        """
        files = []
        files.append("models/engine/file_storage.py")
        files.append("tests/test_models/test_engine/test_file_storage.py")
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(files)
        self.assertEqual(p.total_errors, 0, "pep8 error")

    def test_storage(self):
        """
            test file storage class attribute
        """
        data0 = storage.all().copy()
        data1 = storage.all().copy()
        self.assertEqual(data0, data1, "data0 != data1")
        bmodel = BaseModel()
        data2 = storage.all().copy()
        self.assertNotEqual(
            data1, data2,
            "old data and new data =="
        )

    def test_save(self):
        """
         test if the right data is saved to file
        """
        bmodel0 = BaseModel()
        data0 = storage.all().copy()
        storage.save()
        bmodel1 = BaseModel()
        storage.save()
        storage.reload()
        data1 = storage.all().copy()
        self.assertNotEqual(data0, data1)
