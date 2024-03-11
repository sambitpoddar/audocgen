# Usage Guide

This guide provides detailed instructions on how to use the AuDocGen package to generate comprehensive documentation from Python code.

## Installation

To install AuDocGen, use pip:

```bash
pip install audocgen
```

## Initialization

Initialize an instance of the AuDocGen class with the desired configuration options:

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
```

### Customization Options

- `project_path`: The path to the Python project directory.
- `template_path`: The path to the directory containing custom templates for rendering documentation.
- `output_path`: The path to the directory where the generated documentation will be saved.
- `include_functions`: Flag to include functions/methods in the generated documentation. Default is True.
- `include_classes`: Flag to include classes in the generated documentation. Default is True.

## Generating Documentation

To generate documentation, call the `generate_docs()` method:

```python
# Generate documentation
autodoc.generate_docs(output_format="html")
```

### Output Formats

AuDocGen supports two output formats for generated documentation:

- **HTML**: Renders the documentation in HTML format.
- **Markdown**: Renders the documentation in Markdown format.

## Advanced Usage

AuDocGen supports more advanced usage scenarios, such as generating documentation for multiple modules or the entire project.

### Generating Documentation for Multiple Modules

To generate documentation for multiple modules, use the `project_path` parameter:

```python
# Initialize AuDocGen with project path
autodoc = AuDocGen(
    project_path="path/to/project",
    template_path="path/to/templates",
    output_path="path/to/output",
    include_functions=True,
    include_classes=True
)
```

### Customizing Code Example Extraction

AuDocGen allows customization of the code example extraction logic by defining custom markers or sections within docstrings to indicate code examples.

```python
# Define custom markers or sections within docstrings
# Example:
#     Examples:
#         ```
#         # Your code example here
#         ```
```

## Real-time Examples

Below are real-time examples demonstrating the usage of AuDocGen for generating documentation from Python code:

1. **Generating Documentation for a Python Project**:

```python
from audocgen import AuDocGen

# Initialize AuDocGen with project path
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

2. **Customizing Code Example Extraction**:

```python
from audocgen import AuDocGen

# Define custom markers or sections within docstrings
# Example:
#     Examples:
#         ```
#         # Your code example here
#         ```

# Initialize AuDocGen with custom extraction logic
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

## Contributing

Contributions to AuDocGen are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the [GitHub repository](https://github.com/your_username/audocgen).

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## Acknowledgements

- AuDocGen was inspired by the need for a simple yet powerful Python documentation generator.
- Thanks to the Python community for their valuable contributions and feedback.

---

This guide provides detailed instructions on how to use AuDocGen for generating documentation from Python code, including customization options, advanced usage scenarios, and real-time examples. Feel free to refer to the provided examples and links for further information.
