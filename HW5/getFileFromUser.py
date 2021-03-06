import re   #Required to validate user entry using regular expressions

def getFileFromUser():
    #Collect file name to be opened from User
    print("Enter the name of the file you would like to open:  ")
    fileName = input()

    #Declare regex for testing User entry, if doesn't match, display error and quit
    pattern = re.compile(".+[.].+")
    if not pattern.match(fileName):
        print("\nBad entry. File must be entered: 'fileName.fileExt' \nFor Example: 'foo.txt' \nTry again.")
        exit(0)

    #If file entry is good, split into fileDesc and fileExt
    fileDesc = fileName.split('.')[0]
    fileExt = fileName.split('.')[1]

    return [fileName, fileDesc, fileExt]
