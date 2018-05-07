from parsimonious import NodeVisitor, Grammar


class GraphEntryParser(NodeVisitor):
    grammar = '''
entry = source link_symbol target comma_separated*
source = ~"[0-9]+"
comma_separated = ", " target
target = ~"[0-9]+"
link_symbol = " <-> "
    '''

    def __init__(self, text):
        ast = Grammar(self.grammar).parse(text)
        self.source = None
        self.targets = []
        self.visit(ast)

    def generic_visit(self, node, vc):
        pass

    def visit_source(self, node, vc):
        self.source = int(node.text)

    def visit_target(self, node, vc):
        self.targets.append(int(node.text))


def task02():
    program_graph = {}
    # with open('example_input.txt') as f:
    with open('input.txt') as f:
        for l in [line.rstrip() for line in f]:
            parser = GraphEntryParser(l)
            program_graph[parser.source] = parser.targets

    found_nodes = set()
    number_of_connected_components = 0

    def search_connected_programs(source):
        for target in program_graph[source]:
            if target not in found_nodes:
                found_nodes.add(target)
                search_connected_programs(target)

    for node in program_graph.keys():
        if node not in found_nodes:
            search_connected_programs(node)
            number_of_connected_components += 1

    print(len(found_nodes))
    print(number_of_connected_components)


task02()
