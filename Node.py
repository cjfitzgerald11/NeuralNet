import math
class Node:
    def __init__(self, typeNode):
        self.nodeTypes = {"input": 0, "bias": 1, "output": 2}
        self.nodeType = self.nodeTypes[typeNode]

    def activate(self, input):
        if self.nodeType == 0:
            return input
        elif self.nodeType == 1:
            return 1
        else:
            return 1.0/(1.0 + pow(math.e,(-input + 0.5)))
