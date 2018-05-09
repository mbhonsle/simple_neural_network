from placeholder import Placeholder
from variables import Variable
import numpy as np


class Session:
    def run(self, operation, feed_dict=None):
        if feed_dict is None:
            feed_dict = {}
        nodes_postorder = operation.traverse_postorder()
        for node in nodes_postorder:
            if type(node) == Placeholder:
                node.output = feed_dict[node]
            elif type(node) == Variable:
                node.output = node.value
            else:
                node.inputs = [input_node.output for input_node in node.input_nodes]
                node.output = node.compute(*node.inputs)

            if type(node.output) == list:
                node.output = np.array(node.output)

        return operation.output
