# Customization Guide

This guide provides detailed instructions on customizing the behavior and output of the AuDocGen package to suit your specific documentation needs.

## Customization Options

AuDocGen offers extensive customization options to tailor the generated documentation according to your requirements. These options can be configured during initialization of the `AuDocGen` class.

### Initialization Parameters

When initializing AuDocGen, the following parameters can be specified to customize the documentation generation process:

- **`project_path`**: Path to the Python project directory. If provided, AuDocGen will generate documentation for all modules within the project.
  
- **`module_path`**: Path to the Python module file. If provided, AuDocGen will generate documentation for the specified module.
  
- **`template_path`**: Path to the directory containing custom templates for rendering documentation. Customize the appearance and layout of the generated documentation using custom templates.
  
- **`output_path`**: Path to the directory where the generated documentation will be saved. By default, the documentation is saved in the current working directory.
  
- **`include_functions`**: Flag to include functions/methods in the generated documentation. Default is `True`.
  
- **`include_classes`**: Flag to include classes in the generated documentation. Default is `True`.

## Code Example Extraction

AuDocGen allows customization of the code example extraction logic. Define custom markers or sections within docstrings to indicate code examples. AuDocGen will extract these code examples and include them in the generated documentation.

### Custom Code Example Extraction

Define custom markers or sections within docstrings to indicate code examples:

```python
# Define custom markers or sections within docstrings
def create_user(username, password):
    """
    Create a new user account.

    Parameters:
        username (str): The username for the new user.
        password (str): The password for the new user.

    Examples:
        ```
        # Example usage: Creating a new user
        create_user('john_doe', 'password123')
        ```
    """
    # Function implementation
    new_user = {
        'username': username,
        'password': password
    }
    # Add new_user to database or perform other relevant actions
    return new_user

def delete_user(username):
    """
    Delete a user account.

    Parameters:
        username (str): The username of the user to delete.

    Examples:
        ```
        # Example usage: Deleting a user
        delete_user('john_doe')
        ```
    """
    # Function implementation
    # Delete user from database or perform other relevant actions
    pass

# Initialize AuDocGen with custom code example extraction logic
autodoc = AuDocGen(
    project_path="path/to/project",
    template_path="path/to/templates",
    output_path="path/to/output",
    include_functions=True,
    include_classes=True
)
```

## Custom Templates


You can use custom templates to customize the appearance and layout of the generated documentation. AuDocGen uses the Jinja2 templating engine to render documentation from templates.
### Creating Custom Templates

1. Create a directory to store your custom templates.
2. Create HTML or Markdown files within the directory, using Jinja2 syntax for placeholders and logic.
3. Specify the path to your custom templates directory when initializing AuDocGen.

### Specify Custom Templates Path

Specify the path to your custom templates directory when initializing AuDocGen:

```python
# Initialize AuDocGen with custom template path
autodoc = AuDocGen(
    project_path="path/to/project",
    template_path="path/to/custom/templates",
    output_path="path/to/output",
    include_functions=True,
    include_classes=True
)
```

## Conclusion

Now that you are familiar with the customization options provided by AuDocGen, you can start customizing the behavior and output of the generated documentation to meet your specific requirements. With AuDocGen's extensive customization options, you can tailor the generated documentation to meet your specific requirements. Experiment with different configurations to achieve the desired documentation output.

---

This customization guide provides detailed instructions on customizing the behavior and output of the AuDocGen package, focusing specifically on initialization parameters, code example extraction, and custom templates. Feel free to refer to this guide whenever you need to customize AuDocGen for your documentation needs.
