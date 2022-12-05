"""Project class test module."""

import os
import unittest
from generator.tests import TestBase

from generator.parser import DataParser


class TestProject(TestBase):
    """Test the Project class."""

    def test_normalized_project_name(self):
        """Tests the 'normalized_project_name' property."""
        for project in self.parser.projects:
            normalized_project_name = project.normalized_project_name
            self.assertIsNotNone(normalized_project_name)
            self.assertGreater(len(normalized_project_name), 0)
            print(normalized_project_name)

    def test_technologies_short(self):
        """Tests the Project's technologies_short property."""
        data_file_path = os.path.join(self.test_data_root_path, "projects_with_technology_short.xml")
        parser = DataParser(data_file_path)
        self.assertEqual(len(parser.projects), 1)
        project = parser.projects[0]
        self.assertEqual(project.technologies_short, "C/C++, Objective-C, Java, Kernel driver, Win32, DDK, WDK, HCI (USB), Android, iOS")


if __name__ == '__main__':
    unittest.main(verbosity=2)