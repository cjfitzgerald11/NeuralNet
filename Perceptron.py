from Node import Node
import numpy as np
import random
import math

class Perceptron:
    def __init__(self, numInputNodes,numBiasNodes, numOutputNodes, learningRate):
        self.inputNodes = [True]*numInputNodes
        self.inputNodes += [False]*numBiasNodes
        self.numOutputNodes = numOutputNodes
        self.perceptronGraph = np.zeros((numInputNodes + numBiasNodes,numOutputNodes))
        self.learningRate = learningRate
        self.inputNode = Node("input")
        self.outputNode = Node("output")
        self.biasNode = Node("bias")

    def init(self):
        #initialize perceptron to default values (ranodm number between -1 and 1)
        for outputNode in range(self.numOutputNodes):
            for inputNode in range(len(self.inputNodes)):
                #set initial weight range to be between -0.15 and .15
                weight = random.uniform(-0.15, .15)
                self.setGraphWeight(inputNode,outputNode,weight)

    """Getter method for the edge weight between two nodes."""
    def getGraphWeight(self,inputNode,outputNode):
        return self.perceptronGraph[inputNode,outputNode]

    """Setter method for the edge weight between two nodes."""
    def setGraphWeight(self,inputNode,outputNode,weight):
        self.perceptronGraph[inputNode,outputNode] = weight

    """Based on the edge activation values, this method evaluates an image and
    returns the classified digit."""
    def evaluate(self,image):
        activations,sums = self.getActivations(image)
        if len(activations) == 1:
            """1 output node"""
            activation = activations[0]
            #multiply activation by 10 to get number
            digitEstimate = activation * 10
            #round to get digit
            digit = round(digitEstimate,0)
            #convert to int, remove .0
            digit = int(digit)
            return digit
        else:
            """10 output nodes"""
            maxActivation = 0
            maxIndex = 0
            i = 0
            #select the node with the highest activation
            for activation in activations:
                if activation > maxActivation:
                    maxActivation = activation
                    maxIndex = i
                i += 1
            return maxIndex

    """Method returns a list of the activation values for all of the edges in
    the perceptron graph."""
    def getActivations(self,image):
        activations = []
        sums = []
        #iterate through all actiavtions
        for outputNode in range(self.numOutputNodes):
            sum = 0
            #iterate through all input nodes
            for inputNode in range(len(self.inputNodes)):
                #get weight of edge
                weight = self.getGraphWeight(inputNode,outputNode)
                #cehck for type of node
                isInputNode = self.inputNodes[inputNode]
                if isInputNode:
                    """INPUT NODE"""
                    imageValue = image[inputNode]
                    activation = self.inputNode.activate(imageValue)
                    sum += weight*activation
                else:
                    """BIAS NODE"""
                    activation  = self.biasNode.activate(0)
                    sum += weight*activation
            sums += [sum]
            activations += [self.outputNode.activate(sum)]
        return activations, sums

    """"Trains weights in backprogation manner; compare evaluation with correct
    answer and then adjusts the weights accordingly."""
    def trainWeights(self,trainImage,trainAnswer):
        evaluation = self.evaluate(trainImage)
        activations,sums = self.getActivations(trainImage)
        outputNode = 0
        for activation in activations:
            if len(activations) == 1:
                """1 output node"""
                activation = activation*10
                self.adjustWeight(outputNode, activation, sums[outputNode], trainImage, trainAnswer)
            else:
                """10 output nodes"""
                if outputNode == trainAnswer:
                    self.adjustWeight(outputNode, activation,  sums[outputNode],trainImage,  1)
                else:
                    self.adjustWeight(outputNode, activation,  sums[outputNode], trainImage, 0)
            outputNode += 1

    """Backpropagation adjustment method; updates all weights in perceptron graph
    according to their error and the g_prime value."""
    def adjustWeight(self,outputNode, solution, sum, trainImage, answer):
        err = (answer - solution)/10
        g_prime = self.inputNode.g_prime(sum)
        for inputNode in range(len(self.inputNodes)):
            imageValue = 0
            if self.inputNodes[inputNode] == True:
                imageValue = trainImage[inputNode]
            else:
                imageValue = 1
            currentWeight = self.getGraphWeight(inputNode,outputNode)
            updatedWeight = currentWeight  + (err*g_prime*self.learningRate*(imageValue + .1))
            self.setGraphWeight(inputNode, outputNode,updatedWeight)
