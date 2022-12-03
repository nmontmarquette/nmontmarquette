"""
Test code for readind a XML-based data file.
"""
import xml.etree.ElementTree as ET
from .task import Task


class Project:
    """Wraps a Project data structure object."""

    def __init__(self, node):
        self._node = node
        self._tasks = []
        for children_node in node.find("tasks").findall("task"):
            self._tasks.append(Task(children_node))
        self._details = []
        for line in node.find("details").text.splitlines():
            self._details.append(line.strip())
        self._employer = node.find("employer").text
        self._name = node.find("name").text
        self._technologies = []
        if node.find("technologies"):
            for children in node.find("technologies").findall("technology"):
                self._technologies.append(children.text)
        self._years = node.find("years").text

    @property
    def details(self):
        """Returns extra details about the project."""
        return self._details

    @property
    def employer(self):
        """Returns the project employer."""
        return self._employer

    @property
    def name(self):
        """Returns the project name."""
        return self._name

    @property
    def tasks(self):
        """Returns a collection of Task objects."""
        return self._tasks

    @property
    def technologies(self):
        """Returns a collection of used technology strings."""
        return self._technologies

    @property
    def years(self):
        """Returns the project years active."""
        return self._years

