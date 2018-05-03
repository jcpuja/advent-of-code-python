from parsimonious import NodeVisitor
from parsimonious.grammar import Grammar


class GarbageCountingVisitor(NodeVisitor):

    def __init__(self, _grammar, _text):
        self.garbage_count = 0
        ast = Grammar(_grammar).parse(_text)
        # print(ast)
        self.visit(ast)

    def generic_visit(self, node, visited_children):
        pass

    def visit_character(self, node, garbage):
        self.garbage_count += 1


grammar = """
group = empty_group / non_empty_group
empty_group = group_open group_close
non_empty_group = group_open group_or_garbage_sequence group_close
group_open = "{"
group_close = "}"
group_or_garbage_sequence = group_or_garbage commaed
commaed = comma_group_or_garbage*
comma_group_or_garbage = "," group_or_garbage
group_or_garbage = group / garbage
garbage = "<" text ">"
text = (escaped_character / character)*
character = ~"[^>]"
escaped_character = ~"!."
"""


# text = "{{},{},{},<!!!>>}"
with open('input.txt') as f:
    text = f.readline().rstrip()

visitor = GarbageCountingVisitor(grammar, text)

print(visitor.garbage_count)
