#!/usr/bin/python3

import numpy as np
from Activation_Function import ActivationFunction

class Layer() :
    def __init__(self, num_nodes, inputs, activation_function) :
        self.weights = np.random.rand(num_nodes, inputs)
        self.biases = np.random.rand(num_nodes, 1)
        self.outputs = np.random.rand(num_nodes, 1)
        self.deltas = np.zeros((num_nodes, 1))
        self.activation_function = activation_function

    def feed(self, input_array) :
<<<<<<< HEAD
        # print("Weights", self.weights.shape)
        # print("Inputs ", input_array.shape)
        dot_product = np.dot(self.weights, input_array)
        dot_product += self.biases
        # print("Output: ", dot_product.shape)
=======
        dot_product = np.dot(self.weights, input_array.T) + self.biases
>>>>>>> 403bf66ca3d2c643a6f24c921782b79ed149b4de
        return self.activate(dot_product)

    def activate(self, x) :
        activator = ActivationFunction(self.activation_function)
        return activator.activate(x)

    def calculate_gradients(self, target_or_weights, layer_type, next_layer_deltas=None) :
        activator = ActivationFunction(self.activation_function)
        if layer_type == "output" :
            # print("Output Layer")
            # target_or_weights = target values
            self.deltas = (target_or_weights - self.outputs) * activator.activate(self.outputs, derivative=True)
            # delta = (target - output) * activation_derivative(output)
        else :
            # print("Hidden Layer")
            # target_or_weights = Next layer's weights
            self.deltas = np.dot(target_or_weights.transpose(), next_layer_deltas) * activator.activate(self.outputs, derivative=True)
            # deltas += (next_layers weights * next_layers deltas)
    
    def update_weights(self, inputs, learningRate) :
        change_in_weights = (self.deltas * learningRate) * inputs.transpose()
        self.weights = self.weights + change_in_weights
        self.biases += (self.biases * learningRate)

    def display(self) :
        print("\tWeights: ", self.weights)
        print("\tBiases: ", self.biases)
        print("\tDeltas: ", self.deltas)
        print("\tOutputs: ", self.outputs)
        print("\tActivation: ", self.activation_function)
