from parsimonious import NodeVisitor
from parsimonious.grammar import Grammar


class GroupNode:
    def __init__(self, parsed_node, children):
        self.parsedNode = parsed_node
        self.children = children

    def sum_weight(self, start_weight):
        weight_sum = start_weight
        for child in self.children:
            weight_sum += child.sum_weight(start_weight + 1)

        return weight_sum

    def __str__(self):
        return "{parsed_node=" + self.parsedNode.expr_name \
               + ", children=" + ', '.join(str(child) for child in self.children) \
               + "}"

    __repr__ = __str__


class GroupVisitor(NodeVisitor):

    def __init__(self, _grammar, _text):
        ast = Grammar(_grammar).parse(_text)
        # print(ast)
        self.top_group_node = self.visit(ast)

    def generic_visit(self, node, visited_children):
        pass

    def visit_non_empty_group(self, node, group):
        left_bracket, group_contents, right_bracket = group

        group_node = GroupNode(node, group_contents)
        return group_node

    def visit_empty_group(self, node, group):
        group_node = GroupNode(node, [])
        return group_node

    def visit_commaed(self, node, commaed):
        return list(filter(lambda x: x != 'garbage', commaed))

    def visit_group_or_garbage_sequence(self, node, group_or_garbage_sequence):

        group_or_garbage, commaed = group_or_garbage_sequence

        flat_children = [group_or_garbage]
        flat_children.extend(commaed)

        return list(filter(lambda x: x != 'garbage', flat_children))

    def visit_comma_group_or_garbage(self, node, comma_group_or_garbage):
        comma, group_or_garbage = comma_group_or_garbage
        return group_or_garbage

    def visit_garbage(self, node, garbage):
        return 'garbage'

    visit_group = visit_group_or_garbage = NodeVisitor.lift_child


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


# text = "{{},{},{<abc>},<>}"

with open('input.txt') as f:
    text = f.readline().rstrip()

visitor = GroupVisitor(grammar, text)

group_tree = visitor.top_group_node

# print(group_tree)

print(group_tree.sum_weight(1))
