from numpy import exp, array, random, dot
import time


class NeuralNetwork():
    def __init__(self):
        random.seed(int(time.time()))
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # This is the gradient of the Sigmoid curve.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_inputs)

            error = training_set_outputs - output

            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            self.synaptic_weights += adjustment

    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":

    #Intialise a single neuron neural network.
    neural_network = NeuralNetwork()

    print ("Random starting synaptic weights: ")
    print (neural_network.synaptic_weights)

    training_set_inputs = array([[1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 1, 1],[1,1,0]])
    training_set_outputs = array([[0, 0, 1, 1,0]]).T

    neural_network.train(training_set_inputs, training_set_outputs, 5)

    print ("New synaptic weights after training: ")
    print (neural_network.synaptic_weights)

    # Test the neural network with a new situation.
    print ("Considering new situation [0, 0, 0] -> ?: ")
    print (neural_network.think(array([0, 0, 1])))