import time
from ProblemOne import ProblemOne

def getParams():
    print("Enter the index of the Lucas Number you want calculated: ")
    lucasIndex = input()
    print("\nEnter the timespan in which to calculate the series: ")
    timeSpan = input()

    return [lucasIndex, timeSpan]

if __name__ == "__main__":
    problemOne = ProblemOne()
    
    while True:
        [lucasIndex, timeSpan] = getParams()
        lucasIndex = int(lucasIndex)
        timeSpan = int(timeSpan)
        currIndex = 0

        while currIndex <= lucasIndex:
            try:
               startTime = time.time()
               endTime = startTime + timeSpan
               result = problemOne.calcLucasNumber(currIndex, startTime, endTime)
               print('lucas {0} is {1} - computed with {2} calls in {3} seconds'.format(result[0], result[1], result[2], (timeSpan - (endTime - time.time()))))
               currIndex += 1
               endTime = time.time() + timeSpan
            except TimeoutError as err:
                print('\n\ntimeout at lucas {0} after {1} {2}'.format(currIndex, timeSpan, 'seconds' if timeSpan > 1 else 'second'))
                break