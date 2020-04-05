import time

class ProblemOne(object):
    """Basic implementation for recursively calculating Lucas Numbers"""

    def __init__(self):
        self.lucasZero = 2
        self.lucasOne = 1
        self.numCalls = 0
        self.timeSpan = 0
        self.endTime = 0


    def calcLucasNumber(self, lucasIndex, startTime, timeSpan):
        self.timeSpan = timeSpan
        self.endTime = startTime + timeSpan
        #If lucasIndex or timeSpan requested is negative, return -1 to indicate invalid params
        if(lucasIndex < 0 or timeSpan < 0):
            return -1
        
        def getNextNumber(currIndex, endTime, callCount):
            callCount += 1
            if time.time() > endTime:
                raise TimeoutError("Exceeded timespan")
            elif currIndex < 0:
                print('\nInvalid index')
            elif currIndex == 0:
                result =  [self.lucasZero, callCount]
            elif currIndex == 1:
                result =  [self.lucasOne, callCount]
            else:
                result1 = getNextNumber(currIndex - 1, endTime, callCount)
                result2 = getNextNumber(currIndex - 2, endTime, result1[1])
                result = [result1[0] + result2[0], result2[1]]

            return result
        
        result = getNextNumber(lucasIndex, self.endTime, 0)
        #Reset self.numCalls so I can call method multiple times in one session
        self.numCalls = 0
        #Returns [currLucasNum, numCalls]
        return result