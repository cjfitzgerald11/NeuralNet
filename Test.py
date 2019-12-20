from Perceptron import Perceptron
import numpy as np

class Test:
    def __init__(self,testImages,testAnswers):
        #set of test images
        self.testImages = testImages
        #set of test answers
        self.testAnswers = testAnswers

    """Test method that returns the percentage of correct evaluations that a
    perceptron made during that epoch."""
    def test(self,perceptron):
        #the number of succesful predictions
        numSuccess = 0
        #number of tests run
        numTests = len(self.testImages)
        for i in range(numTests):
            testImage = self.testImages[i]
            testAnswer = self.testAnswers[i]
            #evalute an image with our perceptron
            prediction = perceptron.evaluate(testImage)
            #if the prediciton was correct, increment the number of correct predictions
            if prediction == testAnswer:
                numSuccess += 1
        return numSuccess/numTests
