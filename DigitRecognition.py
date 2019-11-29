from Perceptron import Perceptron
from Train import Train
from Test import Test
from ImageReader import ImageReader

class DigitRecognition:
    def __init__(self, imageDirectory, learningRate, epochs, imageSize,numBiasNodes,numOuputNodes):
        self.learningRate = learningRate
        self.epochs = epochs
        self.imageSize = imageSize
        self.numBiasNodes = numBiasNodes
        self.numOuputNodes = numOuputNodes
        self.ImageReader = ImageReader(imageDirectory)
        Trainer = Train(learningRate)
        Tester = Test()

    def run(self):
        i = 0
        #build defulat perceptron
        Percep = Perceptron(self.imageSize**2, self.numBiasNodes,self.numOuputNodes)
        Percep.init()
        while i < self.epochs:
            Percep,TestResults = self.epoch(Percep)
            print(TestResults)
            i += 1

    def epoch(self,perceptron):
        TrainImages,TrainAnswers,TestImages,TestAnswers = self.getImageSets()
        TrainedPerceptron = Trainer.train(TrainImages,TrainAnswers)
        TestResults = Tester.test(TrainedPerceptron,TrainedPerceptron,TestImages)
        return TrainedPerceptron,TestResults

    def getImageSets(self):
        trainFile = "files/train" + str(imageSize) + ".txt"
        testFile = "files/test" + str(imageSize) + ".txt"
        TrainReader = self.ImageReader(trainFile)
        TestReader = self.ImageReader(testFile)
        #only reads images if it hasn't been called before
        TrainReader.readImages()
        TestReader.readImages()
        TrainImages,TrainAnswers = TrainReader.getImages()
        TestImages,TestAnswers = TestReader.getImages()
        return TrainImages,TrainAnswers,TestImages,TestAnswers
