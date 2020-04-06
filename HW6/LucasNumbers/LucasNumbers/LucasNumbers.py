import sys
from ProblemDrivers import ProblemDrivers

if __name__ == "__main__":
    #Class that contains driver methods for each implementation
    problemDrivers = ProblemDrivers()

    #dispatchTable to choose which solution to run
    problemSolutions = {'1': problemDrivers.problemOneDriver, 
                        '2a': problemDrivers.problemTwoADriver, 
                        '4': problemDrivers.problemFourDriver, 
                        '5': problemDrivers.problemFiveDriver}

    while True:
        print("\nWhich solution would you like demo? (1, 2a, 4, 5): ")
        choice = input()
        if choice in problemSolutions:
            problemSolutions[choice]()
        elif choice == 'q' or choice == 'Q':
            sys.exit(0)
        else:
            print("\nInvalid selection, try again.")