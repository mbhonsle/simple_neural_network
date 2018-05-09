from basic_operation import multiply, add, matmul, Sigmoid
from graph import Graph
from placeholder import Placeholder
from session import Session
from variables import Variable


def basic_test():
    '''
    basic test for z = Ax + b
    '''
    g = Graph()
    A = Variable(10, default_graph=g)
    b = Variable(1, default_graph=g)
    x = Placeholder(default_graph=g)
    y = multiply(A, x)
    z = add(y, b)
    sess = Session()
    result = sess.run(operation=z, feed_dict={x: 10})
    print(result)
    assert result == 101

def matrix_multiplication_test():
    '''
    test for matrix multiplication
    '''
    A = Variable([[10, 20], [30, 40]])
    b = Variable([1,2])
    x = Placeholder()
    y = matmul(A, x)
    z = add(y, b)
    sess = Session()
    result = sess.run(operation=z, feed_dict={x: 10})
    assert len(result) == 2
    assert len(result[0]) == 2
    assert result[0][0] == 101
    assert result[0][1] == 202
    assert result[1][0] == 301
    assert result[1][1] == 402


def neural_network_test():
    '''
    Classifier test
    '''
    x = Placeholder()
    w = Variable([1, 1])
    b = Variable(-5)
    z = add(matmul(w, x), b)
    a = Sigmoid(z)
    sess = Session()
    assert sess.run(operation=a, feed_dict={x : [8, 10]}) > 0.9
    assert sess.run(operation=a, feed_dict={x: [4, -10]}) < 0.1

basic_test()
matrix_multiplication_test()
neural_network_test()