# -*- coding: utf-8 -*-
"""HW3_Neural_Network (3).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xsdcscRqReJNXB15suKSZrD-g52stp88
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import datasets

output = {}

class Dense():
    def __init__(self, n_x, n_y, seed=1):
        self.n_x = n_x
        self.n_y = n_y
        self.seed = seed
        self.initialize_parameters()

    def initialize_parameters(self):
        """
        Argument:
        self.n_x -- size of the input layer
        self.n_y -- size of the output layer
        self.parameters -- python dictionary containing your parameters:
                           W -- weight matrix of shape (n_y, n_x)
                           b -- bias vector of shape (n_y, 1)
        """
        np.random.seed(self.seed)

        # GRADED FUNCTION: linear_initialize_parameters
        ### START CODE HERE ### (≈ 6 lines of code)
        #W = np.random.uniform(low=-limit, high=limit, size=(self.n_x, self.n_y))
        #prroblem: uniform, got error
        #W = np.random.randn(-limit, limit)
        shape = (self.n_y, self.n_x)
        #fan_in = self.n_x
        #fan_out = self.n_y
        #problem:shape for np.zeros cannot simply write  np.zeros(self.n_y, self.n_x)
        W = np.zeros(shape)
        #limit = np.sqrt(6/(self.n_x + self.n_y))
        for i in range(self.n_y):
          for j in range(self.n_x):
            W[i][j] = np.array(np.random.uniform((-1)*(np.sqrt(6/(self.n_x + self.n_y))),(np.sqrt(6/(self.n_x + self.n_y)))))
            #print(W)
        b = np.zeros((self.n_y, 1))*(np.sqrt(6/(self.n_x + self.n_y)))
        ### END CODE HERE ###

        assert(W.shape == (self.n_y, self.n_x))
        assert(b.shape == (self.n_y, 1))

        self.parameters = {"W": W, "b": b}

    def forward(self, A):
        """
        Implement the linear part of a layer's forward propagation.

        Arguments:
        A -- activations from previous layer (or input data): (size of previous layer, number of examples)
        self.cache -- a python tuple containing "A", "W" and "b" ; stored for computing the backward pass efficiently

        Returns:
        Z -- the input of the activation function, also called pre-activation parameter
        """

        # GRADED FUNCTION: linear_forward
        ### START CODE HERE ### (≈ 2 line of code)
        Z = np.dot(self.parameters["W"], A) + self.parameters["b"]
        self.cache = (A, self.parameters["W"] , self.parameters["b"])
        ### END CODE HERE ###

        assert(Z.shape == (self.parameters["W"].shape[0], A.shape[1]))

        return Z

    def backward(self, dZ):
        """
        Implement the linear portion of backward propagation for a single layer (layer l)

        Arguments:
        dZ -- Gradient of the cost with respect to the linear output (of current layer l)
        self.cache -- tuple of values (A_prev, W, b) coming from the forward propagation in the current layer
        self.dW -- Gradient of the cost with respect to W (current layer l), same shape as W
        self.db -- Gradient of the cost with respect to b (current layer l), same shape as b

        Returns:
        dA_prev -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev

        """
        A_prev, W, b = self.cache
        m = A_prev.shape[1]

        # GRADED FUNCTION: linear_backward
        ### START CODE HERE ### (≈ 3 lines of code)
        self.dW = (1./m) * (np.dot(dZ, A_prev.T))
        self.db = (1./m) * (np.sum(dZ, axis=1, keepdims=True))
        dA_prev = np.dot(W.T, dZ)
        ### END CODE HERE ###

        assert (dA_prev.shape == A_prev.shape)
        assert (self.dW.shape == self.parameters["W"].shape)
        assert (self.db.shape == self.parameters["b"].shape)

        return dA_prev

    def update(self, learning_rate):
        """
        Update parameters using gradient descent

        Arguments:
        learning rate -- step size
        """

        # GRADED FUNCTION: linear_update_parameters
        ### START CODE HERE ### (≈ 2 lines of code)
        self.parameters["W"] = self.parameters["W"] - learning_rate * self.dW
        self.parameters["b"] = self.parameters["b"] - learning_rate * self.db
        ### END CODE HERE ###

dense = Dense(3, 1)
print("W = " + str(dense.parameters["W"]))
print("b = " + str(dense.parameters["b"]))

dense = Dense(4, 1)
output["linear_initialize_parameters"] = dense.parameters

A, W, b = np.array([[0, 0.5, 1], [1, 1.5, 2], [2, 2.5, 3]]), np.array([[0.1, 0.2, 0.3]]), np.array([[1.1]])
dense = Dense(3, 1)
dense.parameters = {"W": W, "b": b}
Z = dense.forward(A)
print("Z = " + str(Z))

A, W, b = np.array([[0, -0.5, -1], [1, 1.5, 2], [-2, -2.5, -3]]), np.array([[0.5, 0.3, 0.7]]), np.array([[-1.1]])
dense = Dense(3, 1)
dense.parameters = {"W": W, "b": b}
Z = dense.forward(A)
output["linear_forward"] = (Z, dense.cache)

dZ, linear_cache = np.array([[1.5, 2.5], [0.5, 1.0]]), (np.array([[0.5, 1]]), np.array([[2.0], [1.0]]), np.array([[0.5], [1.0]]))
dense = Dense(1, 2)
dense.cache = linear_cache

dA_prev = dense.backward(dZ)
print ("dA_prev = " + str(dA_prev))
print ("dW = " + str(dense.dW))
print ("db = " + str(dense.db))

dZ, linear_cache = np.array([[0.5, -1.5], [-1.5, 2.0]]), (np.array([[0.25, 1.25]]), np.array([[-1.0], [1.0]]), np.array([[-0.5], [-1.0]]))
dense = Dense(1, 2)
dense.cache = linear_cache
dA_prev = dense.backward(dZ)
output["linear_backward"] = (dA_prev, dense.dW, dense.db)

np.random.seed(1)
dense = Dense(1, 2)
dense.parameters = {"W": np.array([[1.0], [2.0]]), "b": np.array([[0.5], [0.5]])}
dense.dW = np.array([[0.5], [-0.5]])
dense.db = np.array([[1.5], [-1.5]])
dense.update(1.0)
print("W = " + str(dense.parameters["W"]))
print("b = " + str(dense.parameters["b"]))

dense = Dense(3, 4)
np.random.seed(1)
parameters, grads = {"W1": np.random.rand(3, 4), "b1": np.random.rand(3,1), "W2": np.random.rand(1,3), "b2": np.random.rand(1,1)}, {"dW1": np.random.rand(3, 4), "db1": np.random.rand(3,1), "dW2": np.random.rand(1,3), "db2": np.random.rand(1,1)}
dense.parameters = {"W": parameters["W1"], "b": parameters["b1"]}
dense.dW = grads["dW1"]
dense.db = grads["db1"]
dense.update(0.1)
output["linear_update_parameters"] = {"W": dense.parameters["W"], "b": dense.parameters["b"]}

class Activation():
    def __init__(self, function):
        self.function = function

    def forward(self, Z):
        if self.function == "sigmoid":
            """
            Implements the sigmoid activation in numpy

            Arguments:
            Z -- numpy array of any shape
            self.cache -- stores Z as well, useful during backpropagation

            Returns:
            A -- output of sigmoid(z), same shape as Z

            """

            # GRADED FUNCTION: sigmoid_forward
            ### START CODE HERE ### (≈ 8 lines of code)
            value = []
            for i in Z[0]:
              if i >= 0:
                value.append(1/(1 + np.exp(-i)))
              else:
                value.append(np.exp(i)/(1 + np.exp(i)))
            A = np.array([value])
            self.cache = Z
            ### END CODE HERE ###

            return A

        elif self.function == "softmax":
            """
            Implements the softmax activation in numpy

            Arguments:
            Z -- numpy array of any shape (dim 0: number of classes, dim 1: number of samples)
            self.cache -- stores Z as well, useful during backpropagation

            Returns:
            A -- output of softmax(z), same shape as Z
            """

            # GRADED FUNCTION: softmax_forward
            ### START CODE HERE ### (≈ 2 lines of code)
            #A = np.exp(Z - np.max(Z)) / np.exp(Z - np.max(Z)).sum()
            #e_x = np.exp(x - np.max(x))
            A = np.exp(Z - np.max(Z)) / np.exp(Z - np.max(Z)).sum(axis=0)
            self.cache = Z
            #A = None
            #self.cache = Z
            ### END CODE HERE ###

            return A

        elif self.function == "relu":
            """
            Implement the RELU function in numpy
            Arguments:
            Z -- numpy array of any shape
            self.cache -- stores Z as well, useful during backpropagation
            Returns:
            A -- output of relu(z), same shape as Z

            """

            # GRADED FUNCTION: relu_forward
            ### START CODE HERE ### (≈ 2 lines of code)
            A = np.array([[num if num >= 0 else 0 for num in points] for points in Z])
            self.cache = Z
            ### END CODE HERE ###

            assert(A.shape == Z.shape)

            return A

    def backward(self, dA=None, Y=None):
        if self.function == "sigmoid":
            """
            Implement the backward propagation for a single SIGMOID unit.
            Arguments:
            dA -- post-activation gradient, of any shape
            self.cache -- 'Z' where we store for computing backward propagation efficiently
            Returns:
            dZ -- Gradient of the cost with respect to Z
            """

            # GRADED FUNCTION: sigmoid_backward
            ### START CODE HERE ### (≈ 9 lines of code)
            Z = self.cache
            dZ = dA * ((1/(1+np.exp(-Z))) * (1-(1/(1+np.exp(-Z)))))
            ### END CODE HERE ###

            assert (dZ.shape == Z.shape)

            return dZ

        elif self.function == "relu":
            """
            Implement the backward propagation for a single RELU unit.
            Arguments:
            dA -- post-activation gradient, of any shape
            self.cache -- 'Z' where we store for computing backward propagation efficiently
            Returns:
            dZ -- Gradient of the cost with respect to Z
            """

            # GRADED FUNCTION: relu_backward
            ### START CODE HERE ### (≈ 3 lines of code)
            Z = self.cache
            dZ = np.array(dA, copy=True) # just converting dz to a correct object.
            dZ[Z <= 0] = 0 # When z <= 0, you should set dz to 0 as well.
            ### END CODE HERE ###

            assert (dZ.shape == Z.shape)

            return dZ

        elif self.function == "softmax":
            """
            Implement the backward propagation for a [SOFTMAX->CCE LOSS] unit.
            Arguments:
            Y -- true "label" vector (one hot vector, for example: [[1], [0], [0]] represents rock, [[0], [1], [0]] represents paper, [[0], [0], [1]] represents scissors
                                      in a Rock-Paper-Scissors image classification), shape (number of classes, number of examples)
            self.cache -- 'Z' where we store for computing backward propagation efficiently
            Returns:
            dZ -- Gradient of the cost with respect to Z
            """

            # GRADED FUNCTION: softmax_CCE_backward
            ### START CODE HERE ### (≈ 3 lines of code)
            #s  is the output of the softmax function
            #Z is a vector with shape (number of classes K, 1)
            Z = self.cache
            s = self.forward(Z)
            dZ = s-Y
            #print("s = ", s)
            #print("Y= ", Y)
            ### END CODE HERE ###

            assert (dZ.shape == Z.shape)

            return dZ

Z = np.array([[-5, -1, 0, 1, 5]])

sigmoid = Activation("sigmoid")
A = sigmoid.forward(Z)
print("Sigmoid: A = " + str(A))
A = sigmoid.forward(np.array([[-1.82, -0.71, 0.02, 0.13, 2.21]]))
output["sigmoid"] = (A, sigmoid.cache)

relu = Activation("relu")
A = relu.forward(Z)
print("ReLU: A = " + str(A))
A = relu.forward(np.array([[-1.82, -0.71, 0.02, 0.13, 2.21]]))
output["relu"] = (A, relu.cache)

Z = np.array([[1, 0, -2], [2, 1, -1], [3, 0, 0], [4, 0, 1]])
softmax = Activation("softmax")
A = softmax.forward(Z)
print("Softmax: A = \n" + str(A))
A = softmax.forward(np.array([[0.1, 1.2, -2.1], [2.2, 0.7, -1.3], [1.4, 0.3, 0.2], [3.9, 0.5, -1.6]]))
output["softmax"] = (A, softmax.cache)

dA, cache = np.array([[-2, -1.37, -1.14, -2, -3.72]]), np.array([[0, 1, 2, 0, 1]])
sigmoid = Activation("sigmoid")
sigmoid.cache = cache
dZ = sigmoid.backward(dA=dA)
print("Sigmoid: dZ = "+ str(dZ))
dA, cache = np.array([[-2, -2, -1.37, -1.14, -3.72]]), np.array([[2, 0, 1.5, 0, 0.5]])
sigmoid.cache = cache
output["sigmoid_backward"] = sigmoid.backward(dA=dA)

relu = Activation("relu")
dA, cache = np.array([[-2, -1.37, -1.14], [1.7, 2, 3.72]]), np.array([[-2, -1, 2], [1, 0, 1]])
relu.cache = cache
dZ = relu.backward(dA=dA)
print("ReLU: dZ = "+ str(dZ))
dA, cache = np.array([[3.179, -1.376, -0.114], [2.227, -5.612, 4.172]]), np.array([[0.53, 1.21, -2.22], [-1.58, 0.99, -0.11]])
relu.cache = cache
output["relu_backward"] = relu.backward(dA=dA)

Y, cache = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), np.array([[-2, -1, -2], [1, 0, -2], [0, 1, 2]])
softmax = Activation("softmax")
softmax.cache = cache
dZ = softmax.backward(Y=Y)
print("Softmax: dZ = " + str(dZ))
Y, cache = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), np.array([[-2.11, -1.22, -2.33], [1.44, 0.55, -2.66], [0.77, 1.88, 2.99]])
softmax.cache = cache
output["softmax_CCE_backward"] = softmax.backward(Y=Y)

class Model():
    def __init__(self, units, activation_functions):
        self.units = units
        self.activation_functions = activation_functions
        self.initialize_parameters()

    def initialize_parameters(self):
        """
        Arguments:
        self.units -- number of nodes/units for each layer, starting from the input dimension and ending with the output dimension (i.e., [4, 4, 1])
        self.activation_functions -- activation functions used in each layer (i.e, ["relu", "sigmoid"])
        self.linear -- a list to store the dense layers when initializing the model
        self.activation -- a list to store the activation function layers when initializing the model
        """
        self.linear = []
        self.activation = []

        # GRADED FUNCTION: model_initialize_parameters
        ### START CODE HERE ### (≈ 5 lines of code)
        L = len(self.units)
        for i in range(0,L-1):
          self.linear.append(Dense(self.units[i], self.units[i+1], i))
        for j in range(0,(len(self.activation_functions))):
          self.activation.append(Activation(self.activation_functions[j]))
          #print(len(self.activation))
        ### END CODE HERE ###

    def forward(self, X):
        """
        Arguments:
        X -- input data: (number of features, number of examples)

        Returns:
        A -- output of L-layer neural network, probability vector corresponding to your label predictions, shape (number of classes, number of examples)
        """
        A = X
        # GRADED FUNCTION: model_forward
        ### START CODE HERE ### (≈ 4 lines of code)
        #L = len(self.linear)
        for i in range(len(self.linear)):
          A = self.linear[i].forward(A)
          if i < len(self.activation):
            A = self.activation[i].forward(A)

        ### END CODE HERE ###

        return A

    def backward(self, AL=None, Y=None):
        """
        Arguments:
        For multi-class classification,
        AL -- output of L-layer neural network, probability vector corresponding to your label predictions, shape (number of classes, number of examples)
        Y -- true "label" vector (one hot vector, for example: [[1], [0], [0]] represents rock, [[0], [1], [0]] represents paper, [[0], [0], [1]] represents scissors
                              in a Rock-Paper-Scissors image classification), shape (number of classes, number of examples)

        Returns:
        dA_prev -- post-activation gradient
        """

        L = len(self.linear)

        # GRADED FUNCTION: model_backward
        ### START CODE HERE ### (≈ 10 lines of code)
        if self.activation_functions[-1] == "sigmoid":
            # Initializing the backpropagation
            dAL = -1 * (np.divide(Y, AL + 1e-5) - np.divide(1 - Y, 1 - AL + 1e-5))

            # Lth layer (SIGMOID -> LINEAR) gradients. Inputs: "dAL". Outputs: "dA_prev"
            dZ = self.activation[L-1].backward(dAL)
            dA_prev = self.linear[L-1].backward(dZ)
        else:
            # Initializing the backpropagation
            dZ = self.activation[L-1].backward(dA,Y)

            # Lth layer (LINEAR) gradients. Inputs: "dZ". Outputs: "dA_prev"
            dA_prev = self.linear[L-1].backward(dZ)
        #print("Y = ",Y)
        # Loop from l=L-2 to l=0
        # lth layer: (RELU -> LINEAR) gradients.
        # Inputs: "dA_prev". Outputs: "dA_prev"
        for i in reversed(range(L-1)):
            dA_prev = self.activation[i].backward(dA_prev)
            dA_prev = self.linear[i].backward(dA_prev)

        ### END CODE HERE ###

        return dA_prev

    def update(self, learning_rate):
        """
        Arguments:
        learning_rate -- step size
        """

        L = len(self.linear)

        # GRADED FUNCTION: model_update_parameters
        ### START CODE HERE ### (≈ 2 lines of code)
        for i in range(L):
          self.linear[i].update(learning_rate)
          #self.linear[i].parameters["W"] = self.linear[i].parameters["W"] - learning_rate * self.linear[i].dW
          #self.linear[i].parameters["b"] = self.linear[i].parameters["b"] - learning_rate * self.linear[i].db
        ### END CODE HERE ###

model = Model([3, 3, 1], ["relu", "sigmoid"])
print("W1: ", model.linear[0].parameters["W"], "\nb1: ", model.linear[0].parameters["b"])
print("W2: ", model.linear[1].parameters["W"], "\nb2: ", model.linear[1].parameters["b"])

model = Model([16, 8, 1], ["relu", "sigmoid"])
output["model_initialize_parameters"] = (model.linear[0].parameters, model.linear[1].parameters)

A_prev, W, b = np.array([[0.1, -1.2, 1.9], [1.1, 0.2, 2.3], [2.9, -2.5, 3.7]]), np.array([[0.1, 0.2, 0.3]]), np.array([[-0.5]])
model = Model([3, 1], ["sigmoid"])
model.linear[0].parameters = {"W": W, "b": b}
A = model.forward(A_prev)
print("With sigmoid: A = " + str(A))
A_prev, W, b = np.array([[1.1, -2.2], [-3.9, 0.6]]), np.array([[9.1, -8.2]]), np.array([[0.5]])
model = Model([2, 1], ["sigmoid"])
model.linear[0].parameters = {"W": W, "b": b}
A = model.forward(A_prev)
output["model_forward_sigmoid"] = (A, (model.linear[0].cache, model.activation[0].cache))

A_prev, W, b = np.array([[0.1, -1.2, 1.9], [1.1, 0.2, 2.3], [2.9, -2.5, 3.7]]), np.array([[0.1, 0.2, 0.3]]), np.array([[-0.5]])
model = Model([3, 1], ["relu"])
model.linear[0].parameters = {"W": W, "b": b}
A = model.forward(A_prev)
print("With ReLU: A = " + str(A))
A_prev, W, b = np.array([[1.1, -2.2], [-3.9, 0.6]]), np.array([[9.1, -8.2]]), np.array([[0.5]])
model = Model([2, 1], ["relu"])
model.linear[0].parameters = {"W": W, "b": b}
A = model.forward(A_prev)
output["model_forward_relu"] = (A, (model.linear[0].cache, model.activation[0].cache))

A_prev, W, b = np.array([[0.1, -1.2, 1.9], [1.1, 0.2, 2.3], [2.9, -2.5, 3.7]]), np.array([[0.1, 0.2, 0.3], [-0.1, -0.2, -0.3], [-0.1, 0, 0.1]]), np.array([[-0.5], [0.5], [0.1]])
model = Model([3, 3], ["softmax"])
model.linear[0].parameters = {"W": W, "b": b}
A = model.forward(A_prev)
print("With softmax: A = \n" + str(A))
A_prev, W, b = np.array([[-0.1, 1.2, 1.9], [-1.1, 0.2, -2.3], [2.9, -2.5, -3.7]]), np.array([[0.2, 0.2, 0.2], [-0.1, -0.1, -0.1], [-0.1, 0, 0.1]]), np.array([[-0.1], [0.1], [0.5]])
model = Model([3, 3], ["softmax"])
model.linear[0].parameters = {"W": W, "b": b}
A = model.forward(A_prev)
output["model_forward_softmax"] = (A, (model.linear[0].cache, model.activation[0].cache))

# binary classification
X = np.array([[0, 1, 2], [-2, -1, 0], [0.5, 0.5, 0.5]])
model = Model([3, 3, 1], ["relu", "sigmoid"])
AL = model.forward(X)
print("AL = " + str(AL))
print("Length of layers list = " + str(len(model.linear)))

# multi-class classification
X = np.array([[0, 1, 2], [-2, -1, 0], [0.5, 0.5, 0.5]])
model = Model([3, 3, 10], ["relu", "softmax"])
AL = model.forward(X)
print("AL = " + str(AL))
print("Length of layers list = " + str(len(model.linear)))

AL, Y, linear_activation_cache  = np.array([[0.1, 0.2, 0.5, 0.9, 1.0]]), np.array([[0, 0, 1, 1, 1]]), ((np.array([[-2, -1, 0, 1, 2], [2, 1, 0, -1, -2]]), np.array([[2.0, 1.0]]), np.array([[0.5]])), np.array([[0, 1, 2, 0, 1]]))
model = Model([2, 1], ["sigmoid"])
model.linear[0].cache = linear_activation_cache[0]
model.activation[0].cache = linear_activation_cache[1]
dA_prev = model.backward(AL=AL, Y=Y)
print ("sigmoid:")
print ("dA_prev = "+ str(dA_prev))
print ("dW = " + str(model.linear[0].dW))
print ("db = " + str(model.linear[0].db) + "\n")

AL, Y, linear_activation_cache  = np.array([[0.15, 0.23, 0.79, 0.97, 0.99]]), np.array([[0, 0, 1, 1, 1]]), ((np.array([[-2, -1, 0, 1, 2], [2, 1, 0, -1, -2]]), np.array([[2.0, 1.0]]), np.array([[0.5]])), np.array([[0, 1, 2, 0, 1]]))
model = Model([2, 1], ["sigmoid"])
model.linear[0].cache = linear_activation_cache[0]
model.activation[0].cache = linear_activation_cache[1]
dA_prev = model.backward(AL=AL, Y=Y)
output["model_backward_sigmoid"] = (dA_prev, model.linear[0].dW, model.linear[0].db)

X, Y = np.array([[-2, -1, 0, 1, 2], [2, 1, 0, -1, -2]]), np.array([[0, 1, 1, 1, 1]])
model = Model([2, 2, 1], ["relu", "sigmoid"])
AL = model.forward(X)
dA_prev = model.backward(AL=AL, Y=Y)
print ("relu:")
print ("dA_prev = "+ str(dA_prev))
print ("dW = " + str(model.linear[0].dW))
print ("db = " + str(model.linear[0].db) + "\n")

X, Y = np.array([[-2.5, -1.3, 0.1, 1.9, 2.7], [1.2, 2.1, 3.0, -4.1, -5.2]]), np.array([[1, 1, 0, 0, 0]])
model = Model([2, 2, 1], ["relu", "sigmoid"])
AL = model.forward(X)
dA_prev = model.backward(AL=AL, Y=Y)
output["model_backward_relu"] = (dA_prev, model.linear[0].dW, model.linear[0].db)

# binary classification
X, Y = np.array([[0, 1, 2], [-2, -1, 0], [0.5, 0.5, 0.5]]), np.array([[1, 0, 0]])
model = Model([3, 3, 1], ["relu", "sigmoid"])
AL = model.forward(X)

dA_prev = model.backward(AL=AL, Y=Y)
print("Binary classification")
print("dW1 = "+ str(model.linear[0].dW))
print("db1 = "+ str(model.linear[0].db))
print("dA_prev = "+ str(dA_prev) +"\n")

# multi-class classification
X, Y= np.array([[0, 1, 2], [-2, -1, 0], [0.5, 0.5, 0.5]]), np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
model = Model([3, 3, 3], ["relu", "softmax"])
AL = model.forward(X)
dA_prev = model.backward(AL=AL, Y=Y)
print("Multi-class classification")
print("dW1 = "+ str(model.linear[0].dW))
print("db1 = "+ str(model.linear[0].db))
print("dA_prev = "+ str(dA_prev) +"\n")

np.random.seed(1)
parameters, grads = {"W1": np.random.rand(3, 4), "b1": np.random.rand(3,1), "W2": np.random.rand(1,3), "b2": np.random.rand(1,1)}, {"dW1": np.random.rand(3, 4), "db1": np.random.rand(3,1), "dW2": np.random.rand(1,3), "db2": np.random.rand(1,1)}
model = Model([4, 3, 1], ["relu", "sigmoid"])
model.linear[0].parameters = {"W": parameters["W1"], "b": parameters["b1"]}
model.linear[1].parameters = {"W": parameters["W2"], "b": parameters["b2"]}
model.linear[0].dW, model.linear[0].db, model.linear[1].dW, model.linear[1].db = grads["dW1"], grads["db1"], grads["dW2"], grads["db2"]
model.update(0.1)

print ("W1 = "+ str(model.linear[0].parameters["W"]))
print ("b1 = "+ str(model.linear[0].parameters["b"]))
print ("W2 = "+ str(model.linear[1].parameters["W"]))
print ("b2 = "+ str(model.linear[1].parameters["b"]))

np.random.seed(1)
parameters, grads = {"W1": np.random.randn(3, 4), "b1": np.random.randn(3,1), "W2": np.random.randn(1,3), "b2": np.random.randn(1,1)}, {"dW1": np.random.randn(3, 4), "db1": np.random.randn(3,1), "dW2": np.random.randn(1,3), "db2": np.random.randn(1,1)}
model = Model([4, 3, 1], ["relu", "sigmoid"])
model.linear[0].parameters = {"W": parameters["W1"], "b": parameters["b1"]}
model.linear[1].parameters = {"W": parameters["W2"], "b": parameters["b2"]}
model.linear[0].dW, model.linear[0].db, model.linear[1].dW, model.linear[1].db = grads["dW1"], grads["db1"], grads["dW2"], grads["db2"]
model.update(0.075)
output["model_update_parameters"] = {"W1": model.linear[0].parameters["W"], "b1": model.linear[0].parameters["b"], "W2": model.linear[1].parameters["W"], "b2": model.linear[1].parameters["b"]}

# GRADED FUNCTION: compute_BCE_cost

def compute_BCE_cost(AL, Y):
    """
    Implement the binary cross-entropy cost function using the above formula.

    Arguments:
    AL -- probability vector corresponding to your label predictions, shape (1, number of examples)
    Y -- true "label" vector (for example: containing 0 if non-cat, 1 if cat), shape (1, number of examples)

    Returns:
    cost -- binary cross-entropy cost
    """

    m = Y.shape[1]
    #print(AL.shape)
    #print(Y.shape)
    # Compute loss from aL and y.
    ### START CODE HERE ### (≈ 1 line of code)
    cost = np.array((-1/m)*(np.sum(np.multiply(Y,np.log(AL+1e-5)) + np.multiply((1-Y),np.log((1-AL+1e-5))))))
    #np.sum(Y * np.log(AL + 1e-5))
    ### END CODE HERE ###

    cost = np.squeeze(cost)      # To make sure your cost's shape is what we expect (e.g. this turns [[17]] into 17).
    assert(cost.shape == ())

    return cost

AL, Y = np.array([[0.9, 0.6, 0.4, 0.1, 0.2, 0.8]]), np.array([[1, 1, 1, 0, 0, 0]])

print("cost = " + str(compute_BCE_cost(AL, Y)))
output["compute_BCE_cost"] = compute_BCE_cost(np.array([[0.791, 0.983, 0.654, 0.102, 0.212, 0.091, 0.476, 0.899]]), np.array([[1, 1, 1, 1, 0, 0, 0, 0]]))

# GRADED FUNCTION: compute_CCE_cost

def compute_CCE_cost(AL, Y):
    """
    Implement the categorical cross-entropy cost function using the above formula.

    Arguments:
    AL -- probability vector corresponding to your label predictions, shape (number of classes, number of examples)
    Y -- true "label" vector (one hot vector, for example: [[1], [0], [0]] represents rock, [[0], [1], [0]] represents paper, [[0], [0], [1]] represents scissors
                              in a Rock-Paper-Scissors image classification), shape (number of classes, number of examples)

    Returns:
    cost -- categorical cross-entropy cost
    """

    m = Y.shape[1]
    #print(Y.shape)
    # Compute loss from aL and y.
    ### START CODE HERE ### (≈ 1 line of code)
    #cost = (-1/m)*np.dot(np.dot(Y, np.log(AL.T+1e-5)))
    cost = np.array((-1/m)*np.sum(np.multiply(Y,np.log(AL + 1e-5))))
    ### END CODE HERE ###

    cost = np.squeeze(cost)      # To make sure your cost's shape is what we expect (e.g. this turns [[17]] into 17).
    assert(cost.shape == ())

    return cost

AL, Y = np.array([[0.8, 0.6, 0.4, 0.1, 0.2, 0.4], [0.1, 0.3, 0.5, 0.7, 0.1, 0.1], [0.1, 0.1, 0.1, 0.2, 0.7, 0.5]]), np.array([[1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1]])
print("cost = " + str(compute_CCE_cost(AL, Y)))
output["compute_CCE_cost"] = compute_CCE_cost(np.array([[0.711, 0.001, 0.11], [0.099, 0.217, 0.09], [0.035, 0.599, 0.12], [0.068, 0.123, 0.1], [0.087, 0.06, 0.58]]), np.array([[1, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 1]]))

# load breast cancer wisconsin dataset
X, y = datasets.load_breast_cancer(return_X_y=True)
X = X[:500].T
y = np.expand_dims(y[:500], axis=1).T

print("shape of X: " + str(X.shape))
print("shape of y: " + str(y.shape))

# GRADED CODE: binary classification
### START CODE HERE ###
# min max scaling
norm = X
X = (norm - norm.min()) / (norm.max() - norm.min())
### END CODE HERE ###

# split training set and validation set
X_train, y_train = X[:, :400], y[:, :400]
X_val, y_val = X[:, 400:], y[:, 400:]

print("shape of X_train: " + str(X_train.shape) + " shape of y_train: " + str(y_train.shape))
print("shape of X_val: " + str(X_val.shape) + " shape of y_val: " + str(y_val.shape))

# GRADED CODE: binary classification
### START CODE HERE ###
layers_dims = [30,1]
activation_fn = ["sigmoid"]
learning_rate = 0.1
num_iterations = 8500
print_cost = True
classes = 2
costs = []                         # keep track of cost
model = Model(layers_dims, activation_fn)

# Loop (batch gradient descent)
for i in range(0, num_iterations):
    # forward
    AL = model.forward(X_train)
    #print(AL.shape)
    #print(Y.shape)
    # compute cost
    if classes == 2:
        cost = compute_BCE_cost(AL ,y_train)
        #print("2: ", AL.shape)
        #print("2: ", Y.shape)
    else:
        cost = compute_CCE_cost(AL,y_train)
        #print("else: ", AL.shape)
        #print("else: ", Y.shape)
    # backward

    dA_prev = model.backward(AL, y_train)
    #print("bk: ", AL.shape)
    #print("bk: ", Y.shape)

    # update
    model.update(learning_rate)

    if print_cost and i % 100 == 0:
        print ("Cost after iteration %i: %f" %(i, cost))
        costs.append(cost)

# plot the cost
plt.plot(np.squeeze(costs))
plt.ylabel('cost')
plt.xlabel('iterations (per hundreds)')
plt.title("Learning rate =" + str(learning_rate))
plt.show()
### END CODE HERE ###

# Helper function
def predict(X, y, model, classes):
    """
    This function is used to predict the results of a  L-layer neural network.

    Arguments:
    X -- data set of examples you would like to label
    model -- trained model
    classes - number of classes, 2 for binary classification, >2 for multi-class classification

    Returns:
    p -- predictions for the given dataset X
    """

    m = X.shape[1]
    n = len(model.linear) # number of layers in the neural network

    if classes == 2:
      p = np.zeros((1,m))
    else:
      p = np.zeros((classes, m))

    # Forward propagation
    probas = model.forward(X)

    if classes == 2:
      # convert probas to 0/1 predictions
      for i in range(0, probas.shape[1]):
          if probas[0,i] > 0.5:
              p[0,i] = 1
          else:
              p[0,i] = 0

      #print results
      if y is not None:
        print("Accuracy: "  + str(np.sum((p == y)/m)))

    else:
      # convert probas to one hot vector predictions
      prediction = np.argmax(probas, axis=0, out=None)

      for i in range(len(prediction)):
          p[prediction[i], i] = 1

      #print results
      if y is not None:
        correct = 0
        for i in range(m):
          if (p[:, i] == y[:, i]).all():
            correct += 1
        print("Accuracy: "  + str(correct/m))

    return p

pred_train = predict(X_train, y_train, model, 2)

pred_val = predict(X_val, y_val, model, 2)
output["basic_pred_val"] = pred_val
output["basic_layers_dims"] = layers_dims
output["basic_activation_fn"] = activation_fn
basic_model_parameters = []
for basic_linear in model.linear:
  basic_model_parameters.append(basic_linear.parameters)
output["basic_model_parameters"] = basic_model_parameters

# load data
data = np.load("advanced_data.npz")
X_train = data["X_train"]
y_train = data["y_train"].reshape(-1)
X_test = data["X_test"]

# summarize loaded dataset
print('Train: X=%s, y=%s' % (X_train.shape, y_train.shape))
print('Test: X=%s' % (X_test.shape, ))
# plot first few images
for i in range(9):
	# define subplot
	plt.subplot(330 + 1 + i)
	# plot raw pixel data
	plt.imshow(X_train[i], cmap='gray', vmin=0, vmax=255)
# show the figure
plt.show()

# GRADED CODE: multi-class classification (Data preprocessing)
### START CODE HERE ###
#m = 60000
#shuffle_index = np.random.permutation(m)


X_train = X_train / 255.
X_train = X_train.reshape(-1, 28*28)
X_train = X_train.T

X_test = X_test / 255.
X_test = X_test.reshape(-1, 28*28)
X_test = X_test.T

#None
### END CODE HERE ###

print("shape of X_train: " + str(X_train.shape))
print("shape of y_train: " + str(y_train.shape))
print("shape of X_test: " + str(X_test.shape))

# GRADED CODE: multi-class classification (Data preprocessing)
### START CODE HERE ###

digits = 10
examples = y_train.shape[0]
y_train = y_train.reshape(1, examples)
Y_new = np.eye(digits)[y_train.astype('int32')]
y_train = Y_new.T.reshape(digits, examples)

### END CODE HERE ###


print("shape of X_train: " + str(X_train.shape))
print("shape of Y_train: " + str(y_train.shape))
print("shape of X_test: " + str(X_test.shape))

#You can split training and validation set here. (Optional)
### START CODE HERE ###
m = 60000
permutation = list(np.random.permutation(m))
shuffled_X = X_train[:,permutation]
shuffled_Y = y_train[:,permutation]

X_training, y_training = shuffled_X[:, :50000], shuffled_Y[:, :50000]
X_val, y_val = shuffled_X[:, 50000:], shuffled_Y[:, 50000:]


for i in range(9):

	# define subplot
	plt.subplot(330 + 1 + i)
	# plot raw pixel data
	plt.imshow(X_training[:,i].reshape(28,28), cmap='gray', vmin=0, vmax=1)
# show the figure
plt.show()

#print("X: \n", X_train)
#print("Y: \n", y_train)
print("shape of X_val: " + str(X_val.shape))
print("shape of y_val: " + str(y_val.shape))
### END CODE HERE ###

# GRADED CODE: multi-class classification
### START CODE HERE ###
def random_mini_batches(X, Y, mini_batch_size = 64):
    """
    Creates a list of random minibatches from (X, Y)

    Arguments:
    X -- input data, of shape (input size, number of examples)
    Y -- true "label" vector, of shape (number of classes, number of examples)
    mini_batch_size -- size of the mini-batches, integer

    Returns:
    mini_batches -- list of synchronous (mini_batch_X, mini_batch_Y)
    """

    m = X.shape[1]                  # number of training examples
    mini_batches = []
    # Step 1: Shuffle (X, Y)
    permutation = list(np.random.permutation(m))
    shuffled_X = X[:,permutation]
    shuffled_Y = Y[:,permutation]
    #print(X)
    inc = mini_batch_size

    # Step 2 - Partition (shuffled_X, shuffled_Y).
    # Cases with a complete mini batch size only i.e each of 64 examples.
    num_complete_minibatches = math.floor(m / mini_batch_size) # number of mini batches of size mini_batch_size in your partitionning
    for k in range(0, num_complete_minibatches):
        # (approx. 2 lines)
        #mini_batch_X = shuffled_X[:, k * mini_batch_size : (k+1) * mini_batch_size]
        #mini_batch_Y = shuffled_Y[:, k * mini_batch_size: (k+1) * mini_batch_size]
        mini_batch_X = shuffled_X[:, k * mini_batch_size : k * mini_batch_size + mini_batch_size]
        mini_batch_Y = shuffled_Y[:, k * mini_batch_size: k * mini_batch_size + mini_batch_size]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    # For handling the end case (last mini-batch < mini_batch_size i.e less than 64)
    if m % mini_batch_size != 0:
        #(approx. 2 lines)
        #mini_batch_X = shuffled_X[:, (k+1) * mini_batch_size :m]
        #mini_batch_Y = shuffled_Y[:, (k+1) * mini_batch_size :m]
        mini_batch_X = shuffled_X[:, num_complete_minibatches * mini_batch_size : ]
        mini_batch_Y = shuffled_Y[:, num_complete_minibatches * mini_batch_size : ]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    return mini_batches


layers_dims = [784,50,10]
activation_fn = ["relu", "softmax"]
learning_rate = 0.001
num_iterations = 3000
batch_size = 64
print_cost = True
classes = 10
costs = []                         # keep track of cost
model = Model(layers_dims, activation_fn)

# Loop (gradient descent)
for i in range(0, num_iterations):
    mini_batches = random_mini_batches(X_training, y_training, batch_size)
    for batch in mini_batches:
        x_batch, y_batch = batch
        # forward
        AL = model.forward(x_batch)
        #print(AL)
        # compute cost
        if classes == 2:
            cost = compute_BCE_cost(np.array(AL) ,np.array(y_batch))
            #print(cost)
        else:
            cost = compute_CCE_cost(np.array(AL) ,np.array(y_batch))
            #print(cost)
        #print(y_batch)
        # backward
        dA_prev = model.backward(AL, y_batch)
        # update
        model.update(learning_rate)

    if print_cost and i % 100 == 0:
        print ("Cost after iteration %i: %f" %(i, cost))
        costs.append(cost)

# plot the cost
plt.plot(np.squeeze(costs))
plt.ylabel('cost')
plt.xlabel('iterations (per hundreds)')
plt.title("Learning rate =" + str(learning_rate))
plt.show()
### END CODE HERE ###

pred_train = predict(X_train, y_train, model, 10)

#You can check for your validation accuracy here. (Optional)
### START CODE HERE ###
pred_val = predict(X_val, y_val, model, 10)

### END CODE HERE ###

pred_test = predict(X_test, None, model, 10)
output["advanced_pred_test"] = pred_test
output["advanced_layers_dims"] = layers_dims
output["advanced_activation_fn"] = activation_fn
advanced_model_parameters = []
for advanced_linear in model.linear:
  advanced_model_parameters.append(advanced_linear.parameters)
output["advanced_model_parameters"] = advanced_model_parameters

# sanity check
assert(list(output.keys()) == ['linear_initialize_parameters', 'linear_forward', 'linear_backward', 'linear_update_parameters', 'sigmoid', 'relu', 'softmax', 'sigmoid_backward', 'relu_backward', 'softmax_CCE_backward', 'model_initialize_parameters', 'model_forward_sigmoid', 'model_forward_relu', 'model_forward_softmax', 'model_backward_sigmoid', 'model_backward_relu', 'model_update_parameters', 'compute_BCE_cost', 'compute_CCE_cost', 'basic_pred_val', 'basic_layers_dims', 'basic_activation_fn', 'basic_model_parameters', 'advanced_pred_test', 'advanced_layers_dims', 'advanced_activation_fn', 'advanced_model_parameters'])

np.save("output.npy", output)

# sanity check
submit = np.load("output.npy", allow_pickle=True).item()
for key, value in submit.items():
  print(str(key) + "： " + str(type(value)))