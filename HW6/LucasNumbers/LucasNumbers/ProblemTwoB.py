import time

class ProblemTwoB(object):
    """Calculates lucas series by implementing an internal helper function"""

    def __init__(self):
        self.lucasZero = 2
        self.lucasOne = 1
        self.numCalls = 0

    def calcLucasNumber(self, lucasIndex, startTime, timeSpan):
        self.timeSpan = timeSpan
        self.endTime = startTime + timeSpan
        #If lucasIndex or timeSpan requested is negative, return -1 to indicate invalid params
        if(lucasIndex < 0 or timeSpan < 0):
            return -1
        
        def getNextNumber(currIndex):
            self.numCalls += 1
            if time.time() > self.endTime:
                raise TimeoutError("Exceeded timespan")
            elif currIndex < 0:
                print('\nInvalid index')
            elif currIndex == 0:
                result =  [2, self.numCalls]
            elif currIndex == 1:
                result =  [1, self.numCalls]
            else:
                result1 = getNextNumber(currIndex - 1)
                result2 = getNextNumber(currIndex - 2)
                result = [result1[0] + result2[0], result2[1]]

            return result
        
        result = getNextNumber(lucasIndex)

        #Returns [currLucasNum, numCalls]
        return result


