class Problem1(object):
    """Basic implementation for recursively calculating Lucas Numbers"""

    def __init__(self):
        self.lucasZero = 2
        self.lucasOne = 1

    def calcLucasNumber(lucasIndex, startTime, timeSpan):
        #If lucasIndex or timeSpan requested is negative, return -1 to indicate invalid params
        if(lucasIndex < 0 or timeSpan < 0):
            return -1
