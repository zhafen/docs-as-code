import unittest
from textwrap import dedent

from docs_as_code import workflow

class TestMermaidDiagram(unittest.TestCase):
    def test_create_mermaid_diagram(self):

        # Expected mermaid diagram output (this is just an example, adjust as needed)
        expected_mermaid_diagram = dedent("""
        graph TD
            A[add] --> B[return a + b]
            C[result = add(1, 2)]
        """)

        # Create mermaid diagram using the package function
        mermaid_diagram = ""

        # Assert that the created mermaid diagram matches the expected output
        self.assertEqual(mermaid_diagram.strip(), expected_mermaid_diagram.strip())

if __name__ == '__main__':
    unittest.main()
