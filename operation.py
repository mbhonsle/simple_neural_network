
class Operation:
    def __init__(self, input_nodes=None, default_graph=None):

        if input_nodes is None:
            input_nodes = []

        self.input_nodes = input_nodes
        self.output_nodes = []

        for node in self.input_nodes:
            node.output_nodes.append(self)

        if default_graph:
            default_graph.operations.append(self)

    def compute(self):
        pass

    def traverse_postorder(self):
        nodes_postorder = []

        def recurse(node):
            if isinstance(node, Operation):
                for input_node in node.input_nodes:
                    recurse(input_node)
            nodes_postorder.append(node)

        recurse(self)
        return nodes_postorder
