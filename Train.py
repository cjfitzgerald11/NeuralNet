from Perceptron import Perceptron
from Node import Node

class Train:
    def __init__(self, learningRate):
        self.learningRate = learningRate

    def train(self,trainImages,trainAnswers):
        print()
