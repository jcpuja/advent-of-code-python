from parsimonious import NodeVisitor
from parsimonious.grammar import Grammar


class GroupNode:
    def __init__(self, parsed_node, children):
        self.parsedNode = parsed_node
        self.weight = 0
        self.children = children

    def init_weight(self, weight):
        self.weight = weight
        for child in self.children:
            child.init_weight(weight + 1)

    def sum_weight(self):
        weight_sum = self.weight
        for child in self.children:
            weight_sum += child.sum_weight()

        return weight_sum

    def __str__(self):
        return "{parsed_node=" + self.parsedNode.expr_name \
               + ", weight=" + str(self.weight) \
               + ", children=" + ', '.join(str(child) for child in self.children) \
               + "}"

    __repr__ = __str__


class GroupVisitor(NodeVisitor):

    def __init__(self, _grammar, _text):
        ast = Grammar(_grammar).parse(_text)
        print(ast)
        self.top_group_node = self.visit(ast)

    def generic_visit(self, node, visited_children):
        pass

    def visit_group(self, node, group):
        left_bracket, group_contents, right_bracket = group

        group_node = GroupNode(node, group_contents)

        return group_node

    def visit_optional_single_group_or_garbage(self, node, optional_single_group_or_garbage):
        if len(optional_single_group_or_garbage) == 0 or optional_single_group_or_garbage[0] == 'garbage':
            return None

        return optional_single_group_or_garbage[0]

    def visit_comma_separated_groups_or_garbages(self, node, comma_separated_groups_or_garbages):
        return list(filter(lambda x: x != 'garbage', comma_separated_groups_or_garbages))

    def visit_comma_group_or_garbage(self, node, comma_group_or_garbage):
        comma, group_or_garbage = comma_group_or_garbage
        return group_or_garbage

    def visit_garbage(self, node, garbage):
        return 'garbage'

    visit_group_or_garbage = visit_group_or_garbage_sequence = NodeVisitor.lift_child


grammar = """
group = "{" group_or_garbage_sequence "}"
group_or_garbage_sequence = optional_single_group_or_garbage / comma_separated_groups_or_garbages
optional_single_group_or_garbage = group_or_garbage?
comma_separated_groups_or_garbages = group_or_garbage comma_group_or_garbage+
comma_group_or_garbage = "," group_or_garbage
group_or_garbage = group / garbage
garbage = "<" text ">"
text = (escaped_character / character)*
character = ~"[^>]"
escaped_character = ~"!."
"""


text = "{{},{}}"

visitor = GroupVisitor(grammar, text)

group_tree = visitor.top_group_node

group_tree.init_weight(1)

print(group_tree)

print(group_tree.sum_weight())
