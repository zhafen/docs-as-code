import unittest
from textwrap import dedent

from docs_as_code import workflow

class TestMermaidDiagram(unittest.TestCase):
    def test_create_mermaid_diagram(self):

        # Expected mermaid diagram output (this is just an example, adjust as needed)
        expected_mermaid_diagram = dedent("""
        graph TD
            execute --> transform
            transform --> load
        """)

        # Create mermaid diagram using the package function

        class ETLWorkflow(workflow.Workflow):
            def __init__(self):
                super().__init__()

                self.add_node("execute")
                self.add_node("transform")
                self.add_node("load")

                self.add_edge("execute", "transform")
                self.add_edge("transform", "load")

        mermaid_diagram = ""

        # Assert that the created mermaid diagram matches the expected output
        self.assertEqual(mermaid_diagram.strip(), expected_mermaid_diagram.strip())

if __name__ == '__main__':
    unittest.main()
