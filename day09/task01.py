from parsimonious import NodeVisitor
from parsimonious.grammar import Grammar


class GroupVisitor(NodeVisitor):

    node_weights = {}

    counter = 0

    def __init__(self, _grammar, _text):
        ast = Grammar(_grammar).parse(_text)
        self.visit(ast)

    def generic_visit(self, node, visited_children):
        return node

    def visit_group(self, node, visited_children):
        return node



grammar = """
group = "{" (group / garbage)* "}"
garbage = "<" text ">"
text = (escaped_character / character)*
character = ~"[^>]"
escaped_character = ~"!."
"""


text = "{{{{}}}{}}"

GroupVisitor(grammar, text)
