
[![Last commit](https://img.shields.io/github/last-commit/sambitpoddar/audocgen)](https://github.com/your-username/your-repo-name/commits/main)
[![Code Size](https://img.shields.io/github/languages/code-size/your-username/your-repo-name)](https://github.com/your-username/your-repo-name)
[![PyPI version](https://badge.fury.io/py/your-package-name.svg)](https://badge.fury.io/py/your-package-name)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python3.11](https://img.shields.io/badge/Python-3.11-green.svg?style=flat-square)](https://www.python.org/downloads/release/python-2714/) 
[![Downloads](https://pepy.tech/badge/your-package-name)](https://pepy.tech/project/your-package-name)
[![Code style: PEP 8](https://img.shields.io/badge/code%20style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Documentation Status](https://readthedocs.org/projects/your-repo/badge/?version=latest)](https://your-repo.readthedocs.io/en/latest/?badge=latest)

<center><img src="logo.png" alt="AuDocGen Logo" width="280"/></center>

# AuDocGen

AuDocGen is a Python documentation generator designed to simplify the process of creating comprehensive and user-friendly documentation from Python code. It automatically extracts information from docstrings, including API reference documentation and code examples, and renders it into HTML or Markdown format.

## Features

- **Automatic Documentation Generation**: AuDocGen automates the process of generating documentation from Python code, saving developers time and effort.
  
- **Docstring Parsing**: It parses docstrings to extract API reference documentation and code examples, ensuring that the generated documentation is accurate and up-to-date.
  
- **Customization Options**: AuDocGen provides various customization options, allowing users to tailor the generated documentation to their specific needs.

## Installation

You can install AuDocGen using pip:

```bash
pip install audocgen
```

For more detailed installation instructions and troubleshooting, refer to the [Installation Guide](docs/installation.md).

## Usage

To generate documentation using AuDocGen, follow these steps:

1. **Initialization**: Initialize an instance of the AuDocGen class with the desired configuration options.
  
2. **Generation**: Call the `generate_docs()` method to generate the documentation.

Example:

```python
from audocgen import AuDocGen

# Initialize AuDocGen with configuration options
autodoc = AuDocGen(
    project_path="path/to/project",
    template_path="path/to/templates",
    output_path="path/to/output",
    include_functions=True,
    include_classes=True
)

# Generate documentation
autodoc.generate_docs(output_format="html")
```

For more detailed usage examples and advanced scenarios, refer to the [Usage Guide](docs/usage.md).

## Customization Options

AuDocGen provides the following customization options:

- **`project_path`**: The path to the Python project directory. (Required if not specifying `module_path`)

- **`module_path`**: The path to the Python module file. (Required if not specifying `project_path`)

- **`template_path`**: The path to the directory containing custom templates for rendering documentation.

- **`output_path`**: The path to the directory where the generated documentation will be saved.

- **`include_functions`**: Flag to include functions/methods in the generated documentation. Default is True.

- **`include_classes`**: Flag to include classes in the generated documentation. Default is True.

For more detailed information on customization options and their usage, refer to the [Customization Guide](docs/customization.md).

## Documentation Format

AuDocGen supports two output formats for generated documentation:

- **HTML**: Renders the documentation in HTML format.

- **Markdown**: Renders the documentation in Markdown format.

For more information on the documentation format and how to choose the appropriate format for your needs, refer to the [Documentation Format Guide](docs/docuformatguide.md).

## Author

- **Email**: [sambitpoddar@yahoo.com](mailto:sambitpoddar@yahoo.com)
- **LinkedIn**: [Sambit Poddar](https://linkedin.com/in/sambitpoddar)

## Contributing

Contributions to AuDocGen are welcome! If you find any issues or have suggestions for improvement, please [open an issue](https://github.com/sambitpoddar/audocgen/issues) or submit a pull request on the [GitHub repository](https://github.com/sambitpoddar/audocgen).

For guidelines on contributing to AuDocGen and how to get started, refer to the [Contributing Guide](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- AuDocGen was inspired by the need for a simple yet powerful Python documentation generator.

- Thanks to the Python community for their valuable contributions and feedback.

---

Thank you for using AuDocGen!
