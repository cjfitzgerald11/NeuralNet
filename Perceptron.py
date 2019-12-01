import Node from Node
import numpy as np
import random

class Perceptron:
    def __init__(self, numInputNodes,numBiasNodes, numOutputNodes):
        self.inputNodes += [True]*numInputNodes
        self.inputNodes += [False]*numBiasNodes
        self.numOutputNodes = numOutputNodes
        self.perceptronGraph = np.zeros((numInputNodes + numBiasNodes,numOutputNodes))
        self.inputNode = Node("input")
        self.outputNode = Node("output")
        self.biasNode = Node("bias")

    def init(self):
        #initialize perceptron to default values (ranodm number between -1 and 1)
        for outputNode in range(self.numOutputNodes):
            for inputNode in range(len(self.inputNodes)):
                weight = random.uniform(-1.0, 1.0)
                self.setGraphWeight(inputNode,outputNode,weight)

    def getGraphWeight(self,inputNode,outputNode):
        return self.perceptronGraph[inputNode,outputNode]

    def setGraphWeight(self,inputNode,outputNode,weight):
        self.perceptronGraph[inputNode,outputNode] = weight

    def evaluate(self,image):
        activations = self.getActivations(image)
        if len(activations) == 1:
            activation = activations[0]
            digitEstimate = activation * 10
            digit = round(digitEstimate,1)
            return digit
        else:
            maxActivation = 0
            maxIndex = 0
            i = 0
            for activation in activations:
                if activation > maxActivation:
                    maxActivation = activation
                    maxIndex = i
                i += 1
            return maxIndex


    def getActivations(self,image):
        activations = []
        for outputNode in range(self.numOutputNodes):
            sum = 0
            for inputNode in range(len(self.inputNodes)):
                weight = self.getGraphWeight(inputNode,outputNode)
                if inputNode < len(image):
                    imageValue = image[inputNode]
                    activation = self.inputNode.activate(imageValue)
                    sum += weight*activation
                else:
                    activation  = self.inputNode.activate(0)
                    sum += weight*activation
            activations += sum
        return activations
