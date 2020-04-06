import time

def calcLucasNumberVer2C(lucasIndex):
    endTime = calcLucasNumberVer2C.startTime + calcLucasNumberVer2C.timeSpan
    #If lucasIndex or timeSpan requested is negative, return -1 to indicate invalid params
    if(lucasIndex < 0 or calcLucasNumberVer2C.timeSpan < 0):
        return -1
        
    calcLucasNumberVer2C.numCalls += 1
    if time.time() > endTime:
        raise TimeoutError("Exceeded timespan")
    elif lucasIndex < 0:
        print('\nInvalid index')
    elif lucasIndex == 0:
        result =  [2, 1]
    elif lucasIndex == 1:
        result =  [1, 1]
    else:
        result1 = calcLucasNumberVer2C(lucasIndex - 1)
        calcLucasNumberVer2C.numCalls = 1
        result2 = calcLucasNumberVer2C(lucasIndex - 2)
        result = [result1[0] + result2[0], result1[1] + result2[1] + 1]
        
    #Returns [currLucasNum, numCalls]
    return result