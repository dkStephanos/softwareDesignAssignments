import time
import sys
from ProblemOne import ProblemOne
from ProblemFive import ProblemFive
from ProblemTwo import calcLucasNumberVer2

class ProblemDrivers(object):
    def getParams(self):
        print("\nEnter the index of the Lucas Number you want calculated: (enter 'Q' to exit)")
        lucasIndex = input()
        if lucasIndex == 'q' or lucasIndex == 'Q':
            sys.exit(0)
        print("\nEnter the timespan in which to calculate the series: ")
        timeSpan = input()

        return [lucasIndex, timeSpan]

    def problemOneDriver(self):
        problemOne = ProblemOne()
    
        while True:
            [lucasIndex, timeSpan] = self.getParams()
            lucasIndex = int(lucasIndex)
            timeSpan = int(timeSpan)
            currIndex = 0

            while currIndex <= lucasIndex:
                try:
                   startTime = time.time()
                   endTime = startTime + timeSpan
                   tic = time.perf_counter()
                   result = problemOne.calcLucasNumberVer2(currIndex, startTime, timeSpan)
                   toc = time.perf_counter()
                   print('lucas {0} is {1} - computed with {2} {3} in {4:.5f} seconds'.format(currIndex, result[0], result[1], 'call' if result[1] == 1 else 'calls', (toc - tic)))
                   currIndex += 1
                   endTime = time.time() + timeSpan
                except TimeoutError as err:
                    print('\n\ntimeout at lucas {0} after {1} {2}'.format(currIndex, timeSpan, 'seconds' if timeSpan > 1 else 'second'))
                    break

    def problemTwoDriver(self):
        while True:
            [lucasIndex, timeSpan] = self.getParams()
            lucasIndex = int(lucasIndex)
            timeSpan = int(timeSpan)
            currIndex = 0

            while currIndex <= lucasIndex:
                try:
                    startTime = time.time()
                    endTime = startTime + timeSpan
                    tic = time.perf_counter()
                    calcLucasNumberVer2.startTime = startTime
                    calcLucasNumberVer2.timeSpan = timeSpan
                    result = calcLucasNumberVer2(currIndex)
                    toc = time.perf_counter()
                    print('lucas {0} is {1} - computed with {2} {3} in {4:.5f} seconds'.format(currIndex, result[0], result[1], 'call' if result[1] == 1 else 'calls', (toc - tic)))
                    currIndex += 1
                    endTime = time.time() + timeSpan
                except TimeoutError as err:
                    print('\n\ntimeout at lucas {0} after {1} {2}'.format(currIndex, timeSpan, 'seconds' if timeSpan > 1 else 'second'))
                    break


    def problemFiveDriver(self):
        problemFive = ProblemFive()

        while True:
            print("\nEnter the index of the Lucas Number you want calculated: (enter 'Q' to exit)")
            lucasIndex = input()
            if lucasIndex == 'q' or lucasIndex == 'Q':
                sys.exit(0)
            elif len(lucasIndex) > 0:
                lucasNumberFloat = problemFive.calcLucasNumber(int(lucasIndex))
                lucasNumberInt = int(round(lucasNumberFloat))
                lucasNumberDigitCount = len(str(lucasNumberInt))
                print('lucas {0} is {1} -- i.e., {2} -- with {3} {4}'.format(lucasIndex, lucasNumberFloat, lucasNumberInt, lucasNumberDigitCount, 'digit' if lucasNumberDigitCount == 1 else 'digits' ))
