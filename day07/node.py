from typing import List, Dict


class Node:

    def __init__(self, key: str, node_weight: int, child_keys=None):
        if child_keys is None:
            child_keys = []
        self.key = key
        self.node_weight = node_weight
        self.child_keys = child_keys
        self.children: List[Node] = []
        self.tree_weight = -1

    def init_children(self, node_map):
        for child_key in self.child_keys:
            self.children.append(node_map[child_key])

    def compute_tree_weight(self):
        tree_weight = self.node_weight
        for child in self.children:
            tree_weight += child.compute_tree_weight()

        self.tree_weight = tree_weight
        return tree_weight

    def find_unbalanced_node(self, expected_weight=0):
        weight_frequencies: Dict[int, int] = {}
        for child in self.children:
            if child.tree_weight in weight_frequencies:
                weight_frequencies[child.tree_weight] += 1
            else:
                weight_frequencies[child.tree_weight] = 1

        distinct_weights = len(weight_frequencies)
        if distinct_weights == 0 or distinct_weights == 1:
            child_weights = 0
            for child in self.children:
                child_weights += child.tree_weight

            return self, expected_weight - child_weights - self.node_weight

        sorted_weight_frequencies = sorted(list(weight_frequencies.items()), key=lambda tup: tup[1])
        wrong_weight = sorted_weight_frequencies[0][0]
        right_weight = sorted_weight_frequencies[1][0]

        wrong_node = [node for node in self.children if node.tree_weight == wrong_weight][0]

        return wrong_node.find_unbalanced_node(right_weight)
