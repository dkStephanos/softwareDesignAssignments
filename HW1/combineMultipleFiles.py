# Combine contents of three files, writing contents to a fourth user-specified file in what may be a new directory
# return True on success, False on failure

def CombineFiles(files, output_dir, output_file):
    import os                   # Used to create new directory
    openFiles = []
    numProcessed = 0

    # Attempts to open the input files, here 'r' stands for read privaledges
    try:
        for file in files:
            openFiles.push(open(file, 'r'))

    # If we have an issue opening the files, we catch the error here, close whats opened and report the error
    except:
        print("Can't open file {}".format(len(openFiles) + 1)) # prints the file number that threw the error given by len(openFiles) + 1))
        return False
    try:
        os.mkdir(output_dir) # throws exception if diretory already present, catch it and move on to open
    except:
        pass
    try:
        file_4_fd = open(output_file, 'x')  # attempts to open output file, 'x' stands for write privaledges
    except:
        print("Can't open output file")
        return False
    # Next, walk through each file, attempting to write their lines to the output file, stopping if we hit an exception
    while len(openFiles) > 0:
        try:
            for line in openFiles[0]:
                file_4_fd.write(line)
            # When we're done writing to file, close the input file and remove it from our openFiles list
            openFiles[0].close()
            openFiles.pop(0)
            numProcessed += 1
        except Exception as err:
            print("Can't read from file {}: ".format(numProcessed + 1), str(err))
            return False

    # If we get this far, everything worked, so we can return True
    return True

if __name__ == "__main__":
    files = []          # Used to store locations of files to combine as collected from user
    numFiles = input('Please enter the number of files to combine: ')
    # Collects file destinations for the number of files requested to combine
    for value in range(0, numFiles):
        files.push(input('Enter the destination of the file to combine: '))
    # Collects ouput directory and file name for the file containg the combined files
    outputDir = input('Please enter directory for file to create: ')
    outputFile = input('Please enter name of file to create: ')
    CombineFiles(files, outputDir, outputFile)
