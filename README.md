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

For more detailed installation instructions and troubleshooting, refer to the [installation guide](https://github.com/sambitpoddar/audocgen#installation).

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

For more detailed usage examples and advanced scenarios, refer to the [usage guide](https://github.com/sambitpoddar/audocgen#usage).

## Customization Options

AuDocGen provides the following customization options:

- **`project_path`**: The path to the Python project directory. (Required if not specifying `module_path`)

- **`module_path`**: The path to the Python module file. (Required if not specifying `project_path`)

- **`template_path`**: The path to the directory containing custom templates for rendering documentation.

- **`output_path`**: The path to the directory where the generated documentation will be saved.

- **`include_functions`**: Flag to include functions/methods in the generated documentation. Default is True.

- **`include_classes`**: Flag to include classes in the generated documentation. Default is True.

For more detailed information on customization options and their usage, refer to the [customization guide](https://github.com/your_username/audocgen#customization-options).

## Documentation Format

AuDocGen supports two output formats for generated documentation:

- **HTML**: Renders the documentation in HTML format.

- **Markdown**: Renders the documentation in Markdown format.

For more information on the documentation format and how to choose the appropriate format for your needs, refer to the [documentation format guide](https://github.com/your_username/audocgen#documentation-format).

## Author

- **Email**: [sambitpoddar@yahoo.com](mailto:sambitpoddar@yahoo.com)
- **LinkedIn**: [Sambit Poddar](https://linkedin.com/in/sambitpoddar)

## Contributing

Contributions to AuDocGen are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the [GitHub repository](https://github.com/your_username/audocgen).

For guidelines on contributing to AuDocGen and how to get started, refer to the [contributing guide](https://github.com/your_username/audocgen#contributing).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- AuDocGen was inspired by the need for a simple yet powerful Python documentation generator.

- Thanks to the Python community for their valuable contributions and feedback.

---

Feel free to raise an issue for further queries and information.
