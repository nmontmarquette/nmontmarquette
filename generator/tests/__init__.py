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
        return os.path.join("fr_ca", "projects.xml")

    @property
    def parser(self):
        if not self._parser:
            self._parser = DataParser(self.data_file_path)

        return self._parser