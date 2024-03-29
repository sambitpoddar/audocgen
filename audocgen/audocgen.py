# AuDocGen is a Python documentation generator that automatically generates documentation from Python code.
# 
# Author: Sambit Poddar

import inspect
import os
import ast
import markdown2
from jinja2 import Environment, FileSystemLoader
from typing import List, Union
from .code_parser import CodeParser


class AuDocGen:
    """
    Args:
        project_path (str): The path to the Python project directory.
        module_path (str): The path to the Python module file.
        template_path (str): The path to the directory containing custom templates for rendering documentation.
        output_path (str): The path to the directory where the generated documentation will be saved.
        include_functions (bool): Flag to include functions/methods in the generated documentation. Default is True.
        include_classes (bool): Flag to include classes in the generated documentation. Default is True.
    """

    def __init__(self, project_path: str = None, module_path: str = None, template_path: str = None, output_path: str = None, include_functions: bool = True, include_classes: bool = True):
        """
        Initializes an instance of the AuDocGen class.

        Args:
            project_path (str): The path to the Python project directory.
            module_path (str): The path to the Python module file.
            template_path (str): The path to the directory containing custom templates for rendering documentation.
            output_path (str): The path to the directory where the generated documentation will be saved.
            include_functions (bool): Flag to include functions/methods in the generated documentation. Default is True.
            include_classes (bool): Flag to include classes in the generated documentation. Default is True.
        """
        self.project_path = project_path
        self.module_path = module_path
        self.template_path = template_path
        self.output_path = output_path
        self.include_functions = include_functions
        self.include_classes = include_classes
        self.documentation = {}
    

    def generate_docs(self, output_path="docs_output", output_format="html"):
        """
        Generates documentation based on the specified parameters.

        Args:
            output_path (str): The path to the directory where the generated documentation will be saved. Default is 'docs_output'.
            output_format (str): The format of the generated documentation. Supported formats are 'html' and 'md'. Default is 'html'.

        Returns:
            None
        """
        try:
            # Check if project_path or module_path is provided
            if self.project_path:
                self._generate_project_docs(output_format)
            elif self.module_path:
                self._generate_module_docs(output_format)
            else:
                raise ValueError("Either project_path or module_path must be provided.")

            # Generate documentation content
            documentation_content = self._generate_documentation_content()

            # Convert documentation content to the specified format
            if output_format == "html":
                documentation_content = markdown.markdown(documentation_content)
            elif output_format == "md":
                pass  # No conversion needed for Markdown format
            else:
                raise ValueError("Invalid output format. Supported formats: 'html', 'md'.")

            # Load custom template if specified
            if self.template_path:
                template = self._load_template()

            # Render documentation content using the template
                rendered_docs = template.render(documentation_content=documentation_content)

            # Save rendered documentation to output directory
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            with open(os.path.join(output_path, f"documentation.{output_format}"), "w") as f:
                f.write(documentation_content)
              # f.write(rendered_docs) [Use this only if custom template is used]
        except Exception as e:
            print(f"Error generating documentation: {e}")
            
    
    def _load_template(self):
        """
        Loads a custom template from the specified template directory.

        Returns:
            jinja2.Template: The loaded template.
        """
        if not self.template_path:
            raise ValueError("Template path is not specified.")
        
        template_loader = FileSystemLoader(self.template_path)
        template_env = Environment(loader=template_loader)
        template = template_env.get_template("custom_template.jinja2")  # Change the template filename if necessary
        return template
    

    def _generate_documentation_content(self):
        """
        Generates documentation content based on the Python code files in the project directory.

        Returns:
            str: The generated documentation content.
        """
        if not self.project_path:
            raise ValueError("Project path is not specified.")

        documentation_content = ""

        # Traverse project directory and process Python files
        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        module_content = f.read()
                    module_tree = ast.parse(module_content)
                    module_docstring = ast.get_docstring(module_tree)
                    if module_docstring:
                        # Add module docstring to documentation content
                        documentation_content += f"## {file}\n\n"
                        documentation_content += f"{module_docstring}\n\n"
                    for node in module_tree.body:
                        if isinstance(node, ast.FunctionDef) and node.lineno > 1:
                            # Add function docstrings to documentation content
                            function_docstring = ast.get_docstring(node)
                            if function_docstring:
                                documentation_content += f"### {node.name}()\n\n"
                                documentation_content += f"{function_docstring}\n\n"
        return documentation_content


    def _generate_project_docs(self, output_format: str):
        """
        Generates documentation for a Python project.

        Args:
            output_format (str): The format of the generated documentation. Supported formats are 'html' and 'markdown'.

        Returns:
            None
        """
        try:
            modules = self._get_modules_in_project()
            for module in modules:
                self._generate_module_docs(output_format, module)
        except Exception as e:
            print(f"Error generating documentation for project: {e}")

    def _generate_module_docs(self, output_format: str, module: str = None):
        """
        Generates documentation for a Python module.

        Args:
            output_format (str): The format of the generated documentation. Supported formats are 'html' and 'markdown'.
            module (str): The name of the module. If None, uses the module_path provided during initialization.

        Returns:
            None
        """
        try:
            module_name = module or os.path.splitext(os.path.basename(self.module_path))[0]
            module = __import__(module_name)
            self.documentation[module_name] = {
                "functions": [],
                "classes": []
            }

            for name, obj in inspect.getmembers(module):
                if self.include_functions and (inspect.isfunction(obj) or inspect.ismethod(obj)):
                    self._parse_function(obj, module_name)
                elif self.include_classes and inspect.isclass(obj):
                    self._parse_class(obj, module_name)

            self._render_docs(output_format)
        except Exception as e:
            print(f"Error generating documentation for module {module}: {e}")

    def _parse_function(self, func, module_name):
        """
        Parses a function/method and extracts documentation.

        Args:
            func (callable): The function/method object.
            module_name (str): The name of the module containing the function/method.

        Returns:
            None
        """
        try:
            docstring = inspect.getdoc(func)
            if docstring:
                code_examples = self._extract_code_examples(docstring)
                self.documentation[module_name]["functions"].append({
                    "name": func.__name__,
                    "docstring": docstring,
                    "code_examples": code_examples
                })
        except Exception as e:
            print(f"Error parsing function {func.__name__}: {e}")

    def _parse_class(self, cls, module_name):
        """
        Parses a class and extracts documentation.

        Args:
            cls (type): The class object.
            module_name (str): The name of the module containing the class.

        Returns:
            None
        """
        try:
            docstring = inspect.getdoc(cls)
            if docstring:
                code_examples = self._extract_code_examples(docstring)
                self.documentation[module_name]["classes"].append({
                    "name": cls.__name__,
                    "docstring": docstring,
                    "code_examples": code_examples
                })
        except Exception as e:
            print(f"Error parsing class {cls.__name__}: {e}")

    def _extract_code_examples(self, docstring: str) -> List[str]:
        """
        Extracts code examples from a docstring.

        Args:
            docstring (str): The docstring containing code examples.

        Returns:
            List[str]: A list of code examples extracted from the docstring.
        """
        try:
            code_examples = []
            in_code_block = False
            current_example = []

            # Split the docstring into lines
            lines = docstring.split("\n")

            # Iterate through each line of the docstring
            for line in lines:
                # Check for custom marker indicating start of code examples section
                if line.strip().startswith("Examples:") or line.strip().startswith("Code Examples:"):
                    in_code_block = True
                elif in_code_block:
                    # Check for custom marker indicating end of code examples section
                    if line.strip().startswith("End Examples:") or line.strip().startswith("End Code Examples:"):
                        in_code_block = False
                    else:
                        # Accumulate lines within code examples section
                        current_example.append(line.strip())
                elif current_example:
                    # If not in code block but have accumulated lines from previous code example, add to code_examples
                    code_examples.append("\n".join(current_example))
                    current_example = []

            # Add any remaining code example
            if current_example:
                code_examples.append("\n".join(current_example))

            return code_examples
        except Exception as e:
            print(f"Error extracting code examples: {e}")
            return []

    def _render_docs(self, output_format: str):
        """
        Renders the generated documentation.

        Args:
            output_format (str): The format of the generated documentation. Supported formats are 'html' and 'markdown'.

        Returns:
            None
        """
        try:
            template_env = Environment(loader=FileSystemLoader(self.template_path))
            template = template_env.get_template("template.jinja2")
            rendered_docs = template.render(documentation=self.documentation)

            if output_format == "html":
                with open(os.path.join(self.output_path, "index.html"), "w") as f:
                    f.write(rendered_docs)
            elif output_format == "markdown":
                with open(os.path.join(self.output_path, "index.md"), "w") as f:
                    f.write(markdown2.markdown(rendered_docs))
            else:
                raise ValueError("Unsupported output format. Supported formats: 'html', 'markdown'.")
        except Exception as e:
            print(f"Error rendering documentation: {e}")
            
    def _get_modules_in_project(self) -> List[str]:
        """
        Gets a list of module names in the project directory.

        Returns:
            List[str]: A list of module names.
        """
        modules = []
        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.endswith(".py"):
                    module_name = os.path.splitext(file)[0]
                    modules.append(module_name)
        return modules

if __name__ == "__main__":
    # Usage example
    autodoc = AuDocGen(
        project_path="path/to/project",
        template_path="path/to/templates",
        output_path="path/to/output",
        include_functions=True,
        include_classes=True
    )
    autodoc.generate_docs(output_format="html")
