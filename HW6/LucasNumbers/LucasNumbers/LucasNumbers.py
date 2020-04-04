import time

def getParams():
    print("Enter the index of the Lucas Number you want calculated: ")
    lucasIndex = input()
    print("\nEnter the timespan in which to calculate the series: ")
    timeSpan = input()

    return [lucasIndex, timeSpan]

if __name__ == "__main__":
    [lucasIndex, timeSpan] = getParams()