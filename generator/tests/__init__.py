"""Main test module."""

import os
import unittest

from generator.parser import DataParser


class TestBase(unittest.TestCase):
    """Base class for test classes."""
    def setUp(self) -> None:
        self._parser = None
        return super().setUp()

    @property
    def data_file_path(self):
        """Returns data file absolute path."""
        return os.path.join(self.test_data_root_path, "projects.xml")

    @property
    def parser(self):
        if not self._parser:
            self._parser = DataParser(self.data_file_path)

        return self._parser

    @property
    def test_data_root_path(self):
        """Returns the test data absolute root path."""
        this_dir_path = os.path.dirname(os.path.abspath(__file__))
        test_data_path = os.path.join(this_dir_path, "data")
        return test_data_path
