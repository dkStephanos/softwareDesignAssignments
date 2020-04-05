import time

def calcLucasNumberVer2(lucasIndex):
    #If lucasIndex or timeSpan requested is negative, return -1 to indicate invalid params
    if(lucasIndex < 0 or calcLucasNumberVer2.timeSpan < 0):
        return -1
        
    def getNextNumber(currIndex, endTime, callCount):
        callCount += 1
        if time.time() > endTime:
            raise TimeoutError("Exceeded timespan")
        elif currIndex < 0:
            print('\nInvalid index')
        elif currIndex == 0:
            result =  [2, callCount]
        elif currIndex == 1:
            result =  [1, callCount]
        else:
            result1 = getNextNumber(currIndex - 1, endTime, callCount)
            result2 = getNextNumber(currIndex - 2, endTime, result1[1])
            result = [result1[0] + result2[0], result2[1]]

        return result
        
    result = getNextNumber(lucasIndex, calcLucasNumberVer2.startTime + calcLucasNumberVer2.timeSpan, 0)

    #Returns [currLucasNum, numCalls]
    return result