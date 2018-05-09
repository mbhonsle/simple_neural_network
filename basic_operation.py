from operation import Operation
import numpy as np

class add (Operation):

    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x, y):
        self.inputs = [x, y]
        return x + y

class multiply (Operation):

    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x, y):
        self.inputs = [x, y]
        return x * y

class matmul (Operation):

    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x, y):
        '''
        Multiply two numpy matrices
        :param x: numpy matrix
        :param y: numpy matrix
        :return: numpy matrix dot product
        '''
        self.inputs = [x, y]
        return x.dot(y)

class Sigmoid(Operation):
    def __init__(self, z):
        super().__init__([z])

    def compute(self, z):
        return 1 / (1 + np.exp(-z))