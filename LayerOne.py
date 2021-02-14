class LayerOne:
    def __init__(self, input):
        self.input = input
        self.output = [];
        self.setLines()
        self.printLineVals()
        
    def setLines(self):
        self.output.append(self.input[0][0] and self.input[0][1] and self.input[0][2])
        self.output.append(self.input[0][2] and self.input[1][2] and self.input[2][2])
        self.output.append(self.input[0][0] and self.input[1][0] and self.input[2][0])
        self.output.append(self.input[2][0] and self.input[2][1] and self.input[2][2])
        self.output.append(self.input[2][0] and self.input[3][0] and self.input[4][0])
        self.output.append(self.input[2][2] and self.input[3][2] and self.input[4][2])
        self.output.append(self.input[4][0] and self.input[4][1] and self.input[4][2])
    
    def printLineVals(self):
        for x in self.output:
            print(x)

