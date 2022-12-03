"""
Test code for readind a XML-based data file.
"""

class Task:
    """Wraps a Task data structure object."""
    def __init__(self, node):
        self._description = node.find("description").text
        self._technologies = []
        if node.find("technologies"):
            for children in node.find("technologies").findall("technology"):
                self._technologies.append(children.text)

    @property
    def description(self):
        """Returns the task description."""
        return self._description

    @property
    def technologies(self):
        """Returns a collection of used technology strings."""
        return self._technologies
