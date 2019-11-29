class ImageReader:
    def __init__(self,imageFile, imageType):
        self.imageFolder = imageFile
        self.images = []
        self.answers = []
        self.imageType = imageType

    def readImages(self):
        if len(self.images) > 0:
            continue
        else:
            #reads each image in as 1d list of 0 and 1 ints
            #for each image adds is answer to the answers matrix
            #this method does not need to return anything
            input = file.readLines()
            input = [line.strip("\n") for line in input]
            if imageType == 32:
                for i in range(3, len(input), 32):
                    fileString = ''
                    for v in range(32):
                        fileString += input[i + v]
                    self.images += fileString
                    self.answers += input[i + 32]
                print()
            else:
                for line in input:
                    elemList = line.split(',')
                    self.images += elemList[:len(elemList) - 2]
                    self.answers = elemList[-1]

    def getImages(self):
        return self.images, self.answers
