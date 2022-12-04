"""Project class test module."""

import unittest
from generator.tests import TestBase


class TestProject(TestBase):
    """Test the Project class."""

    def test_normalized_project_name(self):
        """Tests the 'normalized_project_name' property."""
        for project in self.parser.projects:
            normalized_project_name = project.normalized_project_name
            self.assertIsNotNone(normalized_project_name)
            self.assertGreater(len(normalized_project_name), 0)
            print(normalized_project_name)


if __name__ == '__main__':
    unittest.main(verbosity=2)