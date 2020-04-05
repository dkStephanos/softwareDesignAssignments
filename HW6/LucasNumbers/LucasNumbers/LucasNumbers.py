import time
from ProblemOne import ProblemOne

def getParams():
    print("Enter the index of the Lucas Number you want calculated: ")
    lucasIndex = input()
    print("\nEnter the timespan in which to calculate the series: ")
    timeSpan = input()

    return [lucasIndex, timeSpan]

def problemOneDriver():
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
               tic = time.perf_counter()
               result = problemOne.calcLucasNumber(currIndex, startTime, timeSpan)
               toc = time.perf_counter()
               print('lucas {0} is {1} - computed with {2} {3} in {4:.5f} seconds'.format(currIndex, result[0], result[1], 'call' if result[1] == 1 else 'calls', (toc - tic)))
               currIndex += 1
               endTime = time.time() + timeSpan
            except TimeoutError as err:
                print('\n\ntimeout at lucas {0} after {1} {2}'.format(currIndex, timeSpan, 'seconds' if timeSpan > 1 else 'second'))
                break

if __name__ == "__main__":
    problemOneDriver()