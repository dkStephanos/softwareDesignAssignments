import time
import globals
from ProblemOne import ProblemOne
from ProblemTwoA import ProblemTwoA
from ProblemTwoB import ProblemTwoB
from ProblemTwoC import calcLucasNumberVer2C
from ProblemFour import ProblemFour
from ProblemFive import ProblemFive

class ProblemDrivers(object):
    def getParams(self):
        while True:
            print("\nEnter the index of the Lucas Number you want calculated: (enter 'Q' to return to main menu)")
            lucasIndex = input()
            #If user chooses to quit, we return -2 as lucasIndex so we know to return back to main
            if lucasIndex == 'q' or lucasIndex == 'Q':
                return [-2, 0]
            print("\nEnter the timespan in which to calculate the series: ")
            timeSpan = input()

            if len(lucasIndex) > 0 and len(timeSpan) > 0:
                return [lucasIndex, timeSpan]

    def getLucasIndex(self):
        while True:
            print("\nEnter the index of the Lucas Number you want calculated: (enter 'Q' to return to main menu)")
            lucasIndex = input()
            #If user chooses to quit, we return -2 so we know to return back to main
            if lucasIndex == 'q' or lucasIndex == 'Q':
                return -2
            elif len(lucasIndex) > 0:
                return int(lucasIndex)

    def problemOneDriver(self):
        problemOne = ProblemOne()
    
        while True:
            [lucasIndex, timeSpan] = self.getParams()
            #If -2, we quit back to main menu
            if lucasIndex == -2:
                return
            lucasIndex = int(lucasIndex)
            timeSpan = int(timeSpan)
            currIndex = 0

            while currIndex <= lucasIndex:
                try:
                   startTime = time.time()
                   tic = time.perf_counter()
                   result = problemOne.calcLucasNumber(currIndex, startTime, timeSpan)
                   problemOne.numCalls = 0
                   toc = time.perf_counter()
                   print('lucas {0} is {1} - computed with {2} {3} in {4:.5f} seconds'.format(currIndex, result[0], result[1], 'call' if result[1] == 1 else 'calls', (toc - tic)))
                   currIndex += 1
                except TimeoutError as err:
                    print('\n\ntimeout at lucas {0} after {1} {2}'.format(currIndex, timeSpan, 'seconds' if timeSpan > 1 else 'second'))
                    break

    def problemTwoADriver(self):
        problemTwoA = ProblemTwoA()
        globals.init()
        while True:
            [lucasIndex, timeSpan] = self.getParams()
            #If -2, we quit back to main menu
            if lucasIndex == -2: 
                return
            lucasIndex = int(lucasIndex)
            globals.timeSpan = int(timeSpan)
            currIndex = 0

            while currIndex <= lucasIndex:
                try:
                   globals.startTime = time.time()
                   tic = time.perf_counter()
                   result = problemTwoA.calcLucasNumber(currIndex)
                   problemTwoA.numCalls = 0
                   toc = time.perf_counter()
                   print('lucas {0} is {1} - computed with {2} {3} in {4:.5f} seconds'.format(currIndex, result[0], result[1], 'call' if result[1] == 1 else 'calls', (toc - tic)))
                   currIndex += 1
                except TimeoutError as err:
                    print('\n\ntimeout at lucas {0} after {1} {2}'.format(currIndex, globals.timeSpan, 'seconds' if globals.timeSpan > 1 else 'second'))
                    break

    def problemTwoBDriver(self):
        problemTwoB = ProblemTwoB()
    
        while True:
            [lucasIndex, timeSpan] = self.getParams()
            #If -2, we quit back to main menu
            if lucasIndex == -2:
                return
            lucasIndex = int(lucasIndex)
            timeSpan = int(timeSpan)
            currIndex = 0

            while currIndex <= lucasIndex:
                try:
                   startTime = time.time()
                   tic = time.perf_counter()
                   result = problemTwoB.calcLucasNumber(currIndex, startTime, timeSpan)
                   problemTwoB.numCalls = 0
                   toc = time.perf_counter()
                   print('lucas {0} is {1} - computed with {2} {3} in {4:.5f} seconds'.format(currIndex, result[0], result[1], 'call' if result[1] == 1 else 'calls', (toc - tic)))
                   currIndex += 1
                except TimeoutError as err:
                    print('\n\ntimeout at lucas {0} after {1} {2}'.format(currIndex, timeSpan, 'seconds' if timeSpan > 1 else 'second'))
                    break

    def problemTwoCDriver(self):
        while True:
            [lucasIndex, timeSpan] = self.getParams()
            if lucasIndex == -2:
                return
            lucasIndex = int(lucasIndex)
            timeSpan = int(timeSpan)
            currIndex = 0

            while currIndex <= lucasIndex:
                try:
                    startTime = time.time()
                    endTime = startTime + timeSpan
                    tic = time.perf_counter()
                    calcLucasNumberVer2C.startTime = startTime
                    calcLucasNumberVer2C.timeSpan = timeSpan
                    calcLucasNumberVer2C.numCalls = 0
                    result = calcLucasNumberVer2C(currIndex)
                    toc = time.perf_counter()
                    print('lucas {0} is {1} - computed with {2} {3} in {4:.5f} seconds'.format(currIndex, result[0], result[1], 'call' if result[1] == 1 else 'calls', (toc - tic)))
                    currIndex += 1
                    endTime = time.time() + timeSpan
                except TimeoutError as err:
                    print('\n\ntimeout at lucas {0} after {1} {2}'.format(currIndex, timeSpan, 'seconds' if timeSpan > 1 else 'second'))
                    break


    def problemFourDriver(self):
        problemFour = ProblemFour()
    
        while True:
            lucasIndex = self.getLucasIndex()
            if lucasIndex == -2:
                return
            currIndex = 0
            while currIndex <= lucasIndex:
                tic = time.perf_counter()
                result = problemFour.calcLucasNumber(currIndex)
                toc = time.perf_counter()
                print('lucas {0} is {1} - computed in {2:.5f} seconds'.format(currIndex, result, (toc - tic)))
                currIndex += 1
                
    def problemFiveDriver(self):
        problemFive = ProblemFive()

        while True:
            lucasIndex = self.getLucasIndex()
            if lucasIndex == -2:
                return
            lucasNumberFloat = problemFive.calcLucasNumber(lucasIndex)
            lucasNumberInt = int(round(lucasNumberFloat))
            lucasNumberDigitCount = len(str(lucasNumberInt))
            print('lucas {0} is {1} -- i.e., {2} -- with {3} {4}'.format(lucasIndex, lucasNumberFloat, lucasNumberInt, lucasNumberDigitCount, 'digit' if lucasNumberDigitCount == 1 else 'digits' ))
