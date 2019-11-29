from Perceptron import Perceptron
from Train import Train
from Test import Test
from ImageReader import ImageReader

class DigitRecognition:
    def __init__(self, imageDirectory, learningRate, epochs, imageSize):
        self.learningRate = learningRate
        self.epochs = epochs
        self.imageSize = imageSize
        self.ImageReader = ImageReader(imageDirectory)
        self.Perceptron = Perceptron()

    def run(self):
        i = 0
        #build defulat perceptron
        Percep = Perceptron()
        Percep.init()
        while i < self.epochs:
            Percep,TestResults = self.epoch(Percep)
            i += 1

    def epoch(self,perceptron):
        TrainImages,TestImages = self.getImageSets()
        Trainer = Train()
        TrainedPerceptron = Trainer.Train(TrainImages)
        Tester = Test()
        TestResults = Tester.Test(TrainedPerceptron,TestImages)
        return TrainedPerceptron,TestResults

    def getImageSets(self):
        trainFile = "files/train" + str(imageSize) + ".txt"
        testFile = "files/test" + str(imageSize) + ".txt"
        TrainReader = self.ImageReader(trainFile)
        TestReader = self.ImageReader(testFile)
        #only reads images if it hasn't been called before
        TrainReader.readImages()
        TestReader.readImages()
        TrainImages = TrainReader.getImages()
        TestImages = TestReader.getImages()
        return TrainImages,TestImages
