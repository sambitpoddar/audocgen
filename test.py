import unittest
from audocgen.audocgen import AuDocGen

class TestAuDocGen(unittest.TestCase):
    def test_generate_docs_for_module(self):
        # Test generating documentation for a module
        autodoc = AuDocGen(module_path="path/to/module.py")
        documentation = autodoc.generate_docs()
        # Assert that documentation is not empty
        self.assertTrue(documentation)

    def test_generate_docs_for_project(self):
        # Test generating documentation for a project
        autodoc = AuDocGen(project_path="path/to/project")
        documentation = autodoc.generate_docs()
        # Assert that documentation is not empty
        self.assertTrue(documentation)

    def test_generate_docs_with_custom_template(self):
        # Test generating documentation with a custom template
        autodoc = AuDocGen(project_path="path/to/project", template_path="path/to/template")
        documentation = autodoc.generate_docs()
        # Assert that documentation is not empty
        self.assertTrue(documentation)

    def test_generate_docs_with_custom_markers(self):
        # Test generating documentation with custom code example markers
        autodoc = AuDocGen(project_path="path/to/project", custom_markers=True)
        documentation = autodoc.generate_docs()
        # Assert that documentation is not empty
        self.assertTrue(documentation)

    def test_generate_docs_for_invalid_path(self):
        # Test generating documentation for an invalid path
        autodoc = AuDocGen(project_path="invalid/path")
        # Assert that an exception is raised
        with self.assertRaises(Exception):
            documentation = autodoc.generate_docs()

    def test_generate_docs_for_empty_project(self):
        # Test generating documentation for an empty project
        autodoc = AuDocGen(project_path="path/to/empty_project")
        documentation = autodoc.generate_docs()
        # Assert that documentation is empty
        self.assertFalse(documentation)

if __name__ == '__main__':
    unittest.main()
