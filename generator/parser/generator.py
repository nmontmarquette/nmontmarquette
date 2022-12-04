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
        self._data_file_path = os.path.join(self.repo_root_path, data_filename)
        if not os.path.exists(self.data_file_path):
            raise FileNotFoundError(f"Couldn't find the '{self.data_file_path}' file")

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

    def _generate_grouped_details_section(self, file, projects):
        file.write("\n<br>\n\n")
        file.write("# Notes et détails\n")
        for project in projects:
            if project.details:
                file.write("\n")
                file.write(f"## {project.employer} - {project.name} ({project.years})\n")
                file.write("\n")
                for line in project.details:
                    file.write(f"{line}\n")

                file.write("\n")
                file.write("------------------------------------------------------------------\n")
                file.write("\n")

    def generate_projects_summary(self, filename, details=False):
        """Generate a project list summary markdown file."""

        with open(filename, "w", encoding="utf-8") as file:
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

            if details:
                self._generate_grouped_details_section(file, self.projects)

    def generate_projects_summary_3_columns(self, filename, details=False):
        """Generate a project list summary markdown file."""

        with open(filename, "w", encoding="utf-8") as file:
            file.write("# Sommaire\n")
            file.write("| Années<br>Employeur<br>Projet | Tâches | Technologies |\n")
            file.write("|:-----------------------------:|--------|--------------|\n")
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
                file.write(f"| {project.years}<br>{project.employer}<br>{project.name} | {tasks_str} | {technologies_str} |\n")

            if details:
                self._generate_grouped_details_section(file, self.projects)

    def generate_tasks_summary(self, filename, details=False):
        """Generates a task list summary markdown file."""

        with open(filename, "w", encoding="utf-8") as file:
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
        """Generates a project list markdown file."""

        with open(filename, "w", encoding="utf-8") as file:

            first_employer = True
            count = 0

            file.write("# Sommaire\n\n")
            for project in self.projects:
                file.write(f"* [{project.years} - {project.name} - {project.technologies_short}](#sdsdsdfsdfsdf)\n")

            file.write("\n\n")
            file.write("# Détails\n\n")

            for project in self.projects:

                # Add a splitter after details (before new employer header)
                # BUT the first time.
                if first_employer is not True:
                    file.write("\n")
                    file.write("------------------------------------------------------------------\n")
                    file.write("<br>\n")
                    file.write("<br>\n")
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

                if show_details and project.details:
                    file.write("\n")
                    file.write("\n")
                    file.write("------------------------------------------------------------------\n")
                    file.write("<br>\n")
                    file.write("\n")
                    file.write("## Notes et détails\n")
                    file.write("\n")
                    for line in project.details:
                        file.write(f"{line}\n")
                    file.write("\n")

    def generate_projects_pages(self, base_folder, use_tech_bullets=True, show_details=True):
        """Generates individual project pages in the specified base folder."""

        links = []
        for project in self.projects:
            filename = f"{project.years}-{project.normalized_project_name}.md"
            filepath = os.path.join(base_folder, filename)
            tasks_str = "<ul>"
            with open(filepath, "w", encoding="utf-8") as file:

                file.write(f"# {project.employer} - {project.name} ({project.years})\n")
                file.write("\n")

                technologies_short = project.technologies_short
                if not technologies_short:
                    technologies_short = "---"
                links.append(f"| **{project.years}** | [{project.name}](./{filepath}) | {technologies_short} |")

                file.write("| Tâches | Technologies |\n")
                file.write("|--------|--------------|\n")

                technologies_str = "<ul>"
                for technology in project.technologies:
                    technologies_str += f"<li>{technology}</li>"

                for task in project.tasks:
                    tasks_str += f"<li>{task.description}</li>"

                    #for technology in task.technologies:
                    #    technologies_str += f"<li>{technology}</li>"

                technologies_str += "</ul>"
                tasks_str += "</ul>"
                file.write(f"| {tasks_str} | {technologies_str} |\n")

                if show_details and project.details:
                    file.write("\n")
                    file.write("# Notes et détails\n")
                    for line in project.details:
                        file.write(f"{line}\n")

        filename = "sommaire.md"
        filepath = os.path.join(base_folder, filename)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write("# Sommaire\n")

            file.write("| Années | Projets | Technologies |\n")
            file.write("|:------:|---------|--------------|\n")
            for link in links:
                file.write(f"{link}\n")

            file.write("\n")
            file.write("------------------------------------------------------------------\n")
