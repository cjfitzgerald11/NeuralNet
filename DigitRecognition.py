from Perceptron import perceptron
from Node import Node
from Train import Train
from Test import Test


class DigitRecognition:
    def __init__(self, problem, learningRate, epochs):
        self.problem = problem
        self.learningRate = learningRate
        self.epochs = epochs
