# Documentation Format Guide

This guide provides information on the documentation formats supported by AuDocGen and how to choose the appropriate format for your needs.

## Supported Formats

AuDocGen supports two output formats for generated documentation:

1. **HTML**: Renders the documentation in HTML format.
2. **Markdown**: Renders the documentation in Markdown format.

### HTML Format

HTML format provides rich formatting options and is suitable for generating documentation with a visually appealing layout. It allows for embedding images, links, and interactive elements, making it ideal for web-based documentation.

### Markdown Format

Markdown format offers simplicity and readability, making it easy to create and maintain documentation. It is platform-independent and can be rendered into various formats, including HTML, PDF, and plaintext.

## Choosing a Format

When choosing a documentation format, consider the following factors:

- **Audience**: Determine the preferences and requirements of your target audience. Some users may prefer HTML for its interactivity, while others may prefer Markdown for its simplicity.

- **Platform Compatibility**: Consider the platform on which the documentation will be viewed. HTML is well-suited for web-based platforms, while Markdown is more versatile and can be rendered on various platforms and devices.

- **Content Complexity**: Evaluate the complexity of your documentation content. HTML provides more advanced formatting options, making it suitable for complex documentation with rich multimedia content. Markdown, on the other hand, is better suited for simpler documentation with primarily textual content.

## Generating Documentation in Different Formats

To generate documentation in the desired format, specify the output format parameter when calling the `generate_docs()` method:

```python
# Generate documentation in HTML format
autodoc.generate_docs(output_format="html")

# Generate documentation in Markdown format
autodoc.generate_docs(output_format="markdown")
```

By choosing the appropriate format for your documentation, you can ensure that it meets the needs and preferences of your audience while effectively conveying the information you want to communicate.

---

This documentation format guide provides information on the supported formats in AuDocGen (HTML and Markdown) and offers guidance on choosing the appropriate format based on audience preferences, platform compatibility, and content complexity. Feel free to refer to this guide when generating documentation with AuDocGen.
