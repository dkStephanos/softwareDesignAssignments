class ProblemFour(object):
    """Calculates lucas number within a loop"""

    def __init__(self):
        self.lucasZero = 2
        self.lucasOne = 1

    def calcLucasNumber(self, lucasIndex):
        #If lucasIndex is negative, return -1 to indicate invalid params
        if(lucasIndex < 0):
            return -1
        
        def getNextNumber(lucasIndex):
            if lucasIndex == 0:
                return self.lucasZero
            elif lucasIndex == 1:
                return self.lucasOne
            else:
                #Initialize our starting values
                kMinus2 = self.lucasZero
                kMinus1 = self.lucasOne

                for index in range(1,lucasIndex):
                    kCurr = kMinus2 + kMinus1
                    kMinus2 = kMinus1
                    kMinus1 = kCurr

                return kCurr


        return getNextNumber(lucasIndex)
