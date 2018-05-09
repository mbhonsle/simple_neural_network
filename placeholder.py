class Placeholder:
    def __init__(self, default_graph=None):
        self.output_nodes = []
        if default_graph:
            default_graph.placeholders.append(self)
