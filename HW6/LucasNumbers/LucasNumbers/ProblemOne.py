import time

class ProblemOne(object):
    """Basic implementation for recursively calculating Lucas Numbers"""

    def __init__(self):
        self.lucasZero = 2
        self.lucasOne = 1
        self.numCalls = 0
        self.timeSpan = 0
        self.endTime = 0


    def calcLucasNumber(self, lucasIndex, startTime, endTime):
        self.timeSpan = endTime - startTime
        self.endTime = endTime
        #If lucasIndex or timeSpan requested is negative, return -1 to indicate invalid params
        if(lucasIndex < 0 or self.timeSpan < 0):
            return -1
        
        def getNextNumber(currIndex, endTime):
            if time.time() > endTime:
                raise TimeoutError("Exceeded timespan")
            elif currIndex < 0:
                print('\nInvalid index')
            elif currIndex == 0:
                result =  [0, self.lucasZero]
            elif currIndex == 1:
                result =  [1, self.lucasOne]
            else:
                currLucasNum = (getNextNumber(currIndex - 2, endTime)[1] if currIndex -2 > 0 else 2) + (getNextNumber(currIndex - 1, endTime)[1] if currIndex - 1 > 1 else 1)
                result = [currIndex, currLucasNum]
            
            self.numCalls += 1
            return result
        
        result = getNextNumber(lucasIndex, self.endTime)
        #Reset self.numCalls so I can call method multiple times in one session
        numCalls = self.numCalls
        self.numCalls = 0
        #Returns [currIndex, currLucasNum, numCalls]
        return [result[0], result[1], numCalls]