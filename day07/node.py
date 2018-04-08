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

    def find_unbalanced_node(self):
        weight_frequencies: Dict[int, int] = {}
        for child in self.children:
            if child.tree_weight in weight_frequencies:
                weight_frequencies[child.tree_weight] += 1
            else:
                weight_frequencies[child.tree_weight] = 1

        distinct_weights = len(weight_frequencies)
        if distinct_weights == 0 or distinct_weights == 1:
            return self

        weight_freq_tuples = list(weight_frequencies.items())
        wrong_weight_tuple = sorted(weight_freq_tuples, key=lambda tup: tup[1])[0]
        wrong_weight = wrong_weight_tuple[0]

        wrong_node = [node for node in self.children if node.tree_weight == wrong_weight][0]

        return wrong_node



