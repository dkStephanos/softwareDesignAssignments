import time
import globals

class ProblemTwoA(object):
    """Basic implementation for recursively calculating Lucas Numbers, but with globals for startTime and timeSpan"""

    def __init__(self):
        self.lucasZero = 2
        self.lucasOne = 1
        self.numCalls = 0

    def calcLucasNumber(self, lucasIndex):
        endTime = globals.startTime + globals.timeSpan
        #If lucasIndex or timeSpan requested is negative, return -1 to indicate invalid params
        if(lucasIndex < 0 or globals.timeSpan < 0):
            return -1
        
        self.numCalls += 1
        if time.time() > endTime:
            raise TimeoutError("Exceeded timespan")
        elif lucasIndex < 0:
            print('\nInvalid index')
        elif lucasIndex == 0:
            result =  [self.lucasZero, 1]
        elif lucasIndex == 1:
            result =  [self.lucasOne, 1]
        else:
            result1 = self.calcLucasNumber(lucasIndex - 1)
            self.numCalls = 1
            result2 = self.calcLucasNumber(lucasIndex - 2)
            result = [result1[0] + result2[0], result1[1] + result2[1] + 1]
        
        #Returns [currLucasNum, numCalls]
        return result