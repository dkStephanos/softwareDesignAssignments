import math

class ProblemFive(object):
    """Finds Lucas numbers using its closed form equation"""

    def __init__(self):
        self.lucasZero = 2
        self.lucasOne = 1
        self.goldenRatio = (1 + math.sqrt(5))/2

    def calcLucasNumber(self, index):
        if index >= 0:
            return (self.goldenRatio ** index) + ((1 - self.goldenRatio) ** index)
        else:
            return -1

