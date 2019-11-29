import Node from Node
import numpy as np

class Perceptron:
    def __init__(self, numInputNodes,numBiasNodes, numOutputNodes):
        self.inputNodes += [True]*numInputNodes
        self.inputNodes += [False]*numBiasNodes
        self.perceptronGraph = np.zeros((numInputNodes + numBiasNodes,numOutputNodes))
        self.inputNode = Node("input")
        self.outputNode = Node("output")
        self.biasNode = Node("bias")

    def self.getGraphWeight(self,inputNode,outputNode):
        return self.perceptronGraph[inputNode,outputNode]

    def getOutputNodeActivation(self,outPu)
