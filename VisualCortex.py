from LayerOne import LayerOne

class VisualCortex:
    def __init__(self, numToGuess):
        print("hello world")
        self.numberMatricies = []
        self.zero = [[True,True,True],[True,False,True],[True,False,True],[True,False,True],[True,True,True]]
        self.numberMatricies.append(self.zero)
        self.one = [[False,False,True],[False,False,True],[False,False,True],[False,False,True],[False,False,True]]
        self.numberMatricies.append(self.one)
        self.two = [[True,True,True],[False,False,True],[True,True,True],[True,False,False],[True,True,True]]
        self.numberMatricies.append(self.two)

        self.printNumToGuess(self.numberMatricies[numToGuess])

        l1 = LayerOne(self.numberMatricies[numToGuess])
        l1Out = l1.output

    def printNumToGuess(self, matrix):
        for x in matrix:
            for y in x:
                if y:
                    print('{:^3s}'.format("*"), end ="")
                else:
                    print("   ", end ="")
            print("")
         

VisualCortex(2)