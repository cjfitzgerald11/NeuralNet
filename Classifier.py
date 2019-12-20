from Perceptron import Perceptron
from Train import Train
from Test import Test
from ImageReader import ImageReader
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

class Classifier:
    def __init__(self,learningRate, epochs, imageSize,numBiasNodes,numOuputNodes):
        self.learningRate = float(learningRate)
        self.epochs = int(epochs)
        self.imageSize = int(imageSize)
        self.numBiasNodes = int(numBiasNodes)
        self.numOuputNodes = int(numOuputNodes)
        self.Trainer = []
        self.Tester = []
        self.testResults = []
        self.runTimes = []

     """Main method that runs the Perceptron algorithm. Initializes a
    Perceptron, trains the Perceptron, and tests it against known dataset."""
    def run(self):
        TrainImages,TrainAnswers,TestImages,TestAnswers = self.getImageSets()
        self.Trainer = Train(TrainImages,TrainAnswers,self.learningRate)
        self.Tester = Test(TestImages,TestAnswers)
        #build defulat perceptron
        Percep = Perceptron(self.imageSize**2, self.numBiasNodes,self.numOuputNodes,self.learningRate)
        Percep.init()
        i = 0
        self.testResults = []
        self.runTimes = []
        startTime = time.process_time()
        while i < self.epochs:
            Percep,TestResults = self.epoch(Percep)
            self.testResults += [TestResults]
            currentTime = time.process_time() - startTime
            self.runTimes += [currentTime]
            i += 1
        return  self.testResults,self.runTimes

    """Helper method that that runs a single training epoch"""
    def epoch(self,perceptron):
        TrainedPerceptron = self.Trainer.train(perceptron)
        TestResults = self.Tester.test(TrainedPerceptron)
        return TrainedPerceptron,TestResults

    def getImageSets(self):
        trainFile = "files/train" + str(imageSize) + ".txt"
        testFile = "files/test" + str(imageSize) + ".txt"
        TrainReader = ImageReader(trainFile,self.imageSize)
        TestReader = ImageReader(testFile,self.imageSize)
        #only reads images if it hasn't been called before
        TrainReader.readImages()
        TestReader.readImages()
        TrainImages,TrainAnswers = TrainReader.getImages()
        TestImages,TestAnswers = TestReader.getImages()
        return TrainImages,TrainAnswers,TestImages,TestAnswers

    def graphResults(self):
        #make test results percents
        testResults = [100*result for result in self.testResults]
        plt.plot(self.runTimes,testResults)
        plt.title("Run Time (s) vs. % Correct")
        plt.xlabel("Run Time (s)")
        plt.ylabel("% Correct")
        plt.show()
        plt.cla()

        epochs = np.arange(1,self.epochs + 1)
        ax = plt.figure().gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.plot(epochs,testResults)
        plt.title("Epochs vs. % Correct")
        plt.xlabel("Epoch")
        plt.ylabel("% Correct")
        plt.show()

#Get Terminal Input
learningRate = sys.argv[1]
epochs = sys.argv[2]
imageSize = sys.argv[3]
numBiasNodes = sys.argv[4]
numOuputNodes = sys.argv[5]

numRuns = 5
classify = Classifier(learningRate,epochs,imageSize,numBiasNodes,numOuputNodes)
allTestResults = []
allRunTimes = []
for i in range(numRuns):
    print("run: ", i + 1)
    testResults,runTimes = classify.run()
    allTestResults += [testResults]
    allRunTimes += [runTimes]
averageTest = np.mean(allTestResults, axis=0)
averageTest = [100*result for result in averageTest]
print("Average Test Success: ", averageTest)
averageRunTimes = np.mean(allRunTimes, axis=0)
print("Average Run Time: ", list(averageRunTimes))
print("maxValue: ", max(averageTest))
