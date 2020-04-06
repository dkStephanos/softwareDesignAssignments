import time

class ProblemThree(object):
    """Calculates Lucas series and returns requested Lucas value and the previous Lucas value"""

    def __init__(self):
        self.lucasZero = 2
        self.lucasOne = 1
        self.numCalls = 0

    def calcLucasNumber(self, lucasIndex, startTime, timeSpan):
        endTime = startTime + timeSpan
        #If lucasIndex or timeSpan requested is negative, return -1 to indicate invalid params
        if(lucasIndex < 0 or timeSpan < 0):
            return -1
        
        self.numCalls += 1
        if time.time() > endTime:
            raise TimeoutError("Exceeded timespan")
        elif lucasIndex < 0:
            print('\nInvalid index')
        elif lucasIndex == 0:
            result =  [self.lucasZero, None, 1]
        elif lucasIndex == 1:
            result =  [self.lucasOne, self.lucasZero, 1]
        else:
            result1 = self.calcLucasNumber(lucasIndex - 1, startTime, timeSpan)
            result = [result1[0] + result1[1], result1[0], result1[2] + 1]
        
        #Returns [currLucasNum, numCalls]
        return result


