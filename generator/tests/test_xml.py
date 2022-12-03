"""Main test module."""
import os
import unittest

from generator.parser import DataParser


class TestXml(unittest.TestCase):
    """Test class for the 'DataParser' class."""

    def test_constructor(self):
        """Simple test reading main XML data file."""
        DataParser("projects.xml")

    def test_constructor_file_not_found(self):
        """Test for exception on non-existing file."""
        with self.assertRaises(FileNotFoundError):
            DataParser("non-existing-file.xml")

    def test_property_root(self):
        """Test the 'root' property."""
        data = DataParser("projects.xml")
        self.assertIsNotNone(data.root)

    def test_property_projects(self):
        """Test the 'projects' property."""
        data = DataParser("projects.xml")
        self.assertIsNotNone(data.projects)
        for project in data.projects:
            self.assertIsNotNone(project.details)
            for line in project.details:
                print(line)
            self.assertIsNotNone(project.employer)
            self.assertIsNotNone(project.tasks)
            self.assertIsNotNone(project.years)
            for task in project.tasks:
                self.assertIsNotNone(task.description)
                self.assertIsNotNone(task.technologies)
                for technology in task.technologies:
                    self.assertIsNotNone(technology)

    def test_generate_tasks_summary(self):
        data = DataParser("projects.xml")
        data.generate_tasks_summary(os.path.join("generated","tasks_summary.md"))

    def test_generate_projects_summary(self):
        data = DataParser("projects.xml")
        data.generate_projects_summary(os.path.join("generated","projects_summary.md"))

    def test_generate_detailed_project_list(self):
        data = DataParser("projects.xml")
        data.generate_project_list(os.path.join("generated","detailed_project_list.md"), show_details=True)

    def test_generate_project_list(self):
        data = DataParser("projects.xml")
        data.generate_project_list(os.path.join("generated","project_list.md"), show_details=False)


if __name__ == '__main__':
    unittest.main(verbosity=2)