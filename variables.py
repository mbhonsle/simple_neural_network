class Variable:
    def __init__(self, initial_value=None, default_graph=None):
        self.value = initial_value
        self.output_nodes = []
        if default_graph:
            default_graph.variables.append(self)
