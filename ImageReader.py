class ImageReader:
    def __init__(self,imageFile):
        self.imageFolder = imageFile
        self.images = []
        self.answers = []

    def readImages(self):
        if len(self.images) > 0:
            continue
        else:
            #reads each image in as 1d list of 0 and 1 ints
            #for each image adds is answer to the answers matrix
            #this method does not need to return anything
            print()

    def getImages(self):
        return self.images, self.answers
