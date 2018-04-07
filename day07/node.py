from typing import List


class Node:

    def __init__(self, key: str, weight: int, children: List[str]=None):
        if children is None:
            children = []
        self.key = key
        self.weight = weight
        self.children = children
