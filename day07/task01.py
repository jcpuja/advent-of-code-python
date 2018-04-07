from day07.node import Node


def parse_input_line(full_str):
    node_and_children = full_str.split(' -> ')
    if len(node_and_children) > 1:
        _children = node_and_children[1].split(", ")
    else:
        _children = []
    key_and_weight = node_and_children[0].split()
    _key = key_and_weight[0]
    _weight = int(key_and_weight[1].strip("()"))

    return _key, _weight, _children


nodes = {}
all_keys = set()
children_keys = set()

with open('input.txt') as file:
    for line in file:
        key, weight, children = parse_input_line(line.rstrip())
        nodes[key] = Node(key, weight, children)
        all_keys.add(key)
        for child in children:
            children_keys.add(child)

print(list(all_keys - children_keys))
