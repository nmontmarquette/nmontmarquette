"""
Test code for readind a XML-based data file.
"""
import os
import xml.etree.ElementTree as ET

from .project import Project


class DataParser():
    """
    Class for parsing consumming data structure.

    Ref.: https://www.edureka.co/blog/python-xml-parser-tutorial/
    """
    def __init__(self, data_filename, locale = "fr_ca"):
        """_summary_

        :param data_filename: _description_
        :type data_filename: _type_
        :param locale: _description_, defaults to "fr_ca"
        :type locale: str, optional
        :raises FileNotFoundError: _description_
        """
        self._projects = None
        self._repo_root_path = None
        self._locale = locale
        self._data_file_path = os.path.join(self.repo_root_path, locale, data_filename)
        if not os.path.exists(self.data_file_path):
            raise FileNotFoundError()

        self._data_tree = ET.parse(self.data_file_path)

    @property
    def data_file_path(self):
        """Returns data file absolute path."""
        return self._data_file_path

    @property
    def repo_root_path(self):
        """Returns the repository absolute root path."""
        if not self._repo_root_path:
            this_dir_path = os.path.dirname(os.path.abspath(__file__))
            self._repo_root_path = os.path.abspath(os.path.join(this_dir_path, os.pardir, os.pardir))

        return self._repo_root_path

    @property
    def root(self):
        """Returns data structure root node."""
        return self._data_tree.getroot()

    @property
    def projects(self):
        """Returns a collection of projects."""
        if not self._projects:
            self._projects = []
            for node in self.root.findall("project"):
                self._projects.append(Project(node))

        return self._projects
        projects = ET.SubElement(self.root[0], "projects")
        pp = ET.SubElements(self.root[0], "projects")
        return ET.SubElement(self.root[0], "projects")

    def generate_projects_summary(self, filename):
        with open(filename, "w") as file:
            file.write("# Sommaire\n")
            file.write("| Années | Employeur | Projet | Tâches | Technologies |\n")
            file.write("|--------|-----------|--------|--------|--------------|\n")
            for project in self.projects:
                tasks_str = "<ul>"

                technologies_str = "<ul>"
                for technology in project.technologies:
                    technologies_str += f"<li>{technology}</li>"

                for task in project.tasks:
                    tasks_str += f"<li>{task.description}</li>"

                    #for technology in task.technologies:
                    #    technologies_str += f"<li>{technology}</li>"

                technologies_str += "</ul>"
                tasks_str += "</ul>"
                file.write(f"| {project.years} | {project.employer} | {project.name} | {tasks_str} | {technologies_str} |\n")

    def generate_tasks_summary(self, filename):
        with open(filename, "w") as file:
            file.write("# Sommaire\n")
            file.write("| Années | Employeur | Projet | Tâches | Technologies |\n")
            file.write("|--------|-----------|--------|--------|--------------|\n")
            for project in self.projects:
                for task in project.tasks:
                    technologies_str = "<ul>"
                    for technology in task.technologies:
                        technologies_str += f"<li>{technology}</li>"
                    technologies_str += "</ul>"
                    file.write(f"| {project.years} | {project.employer} | {project.name} | {task.description} | {technologies_str} |\n")

    def generate_project_list(self, filename, use_tech_bullets=True, show_details=True):
        """Generate a project list markdown file."""

        with open(filename, "w") as file:

            first_employer = True
            count = 0
            for project in self.projects:

                # Add a splitter after details (before new employer header)
                # BUT the first time.
                if first_employer is not True:
                    file.write("\n")
                    file.write("------------------------------------------------------------------\n")
                    file.write("\n")

                file.write(f"# {project.employer} - {project.name} ({project.years})\n")
                file.write("\n")
                first_employer = False
                count += 1

                file.write("| Projet | Tâches | Technologies |\n")
                file.write("|--------|--------|--------------|\n")

                if use_tech_bullets:
                    technologies_str = "<ul>"
                    for technology in project.technologies:
                        technologies_str += f"<li>{technology}</li>"
                    technologies_str += "</ul>"
                else:
                    technologies_str = ""
                    for technology in project.technologies:
                        technologies_str += f"{technology}, "
                    technologies_str = technologies_str[:-2]

                tasks_str = "<ul>"
                for task in project.tasks:
                    tasks_str += f"<li>{task.description}</li>"
                tasks_str += "</ul>"

                file.write(f"| {project.name} | {tasks_str} | {technologies_str} |\n")

                file.write("\n")
                file.write("------------------------------------------------------------------\n")
                file.write("\n")
                if show_details:
                    file.write("## Notes et détails\n")
                    file.write("\n")
                    for line in project.details:
                        file.write(f"{line}\n")
                    file.write("\n")

