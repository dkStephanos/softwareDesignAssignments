# split an input file into mulitiple output files,
# one line fromt he input file to each output file,
# with all output files sharing a common prefix
# and each having the numgber of the line read as its suffix (standardized with preceeding zeros for sorting)

# Pulls in mathmatic methods to calculate number of digits in output file count
from math import ceil, floor, log10

# - determines how many digits are in file count to properly add preceeding zeros
def base_10_digits_in(x):
    return 0 if x == 0 else floor(log10(x)) + 1

# Returns the file name with correct prefix and line numgber
def GetFileName(prefix, lineCount, lineNumber)
    return "{}{{:>0{}}}.txt".format(prefix, base_10_digits_in(lineCount), lineNumber)

# Creates the next output file with passed fileName and writes the line to it, then closes the files
def WriteLineToNewFile(fileName, line):
    try:
        file_fd = open(fileName, 'x')  # here, x means open with edit privaledges
    except:
        print("Error opening file {}".format(fileName))
        return None

    file_fd.write(line)
    file_fd.close()

if __name__ == "__main__":
    source_file = input("enter the name of the file to split: ")
    target_prefix = input("enter the prefix of the target file: ")
    with open(source_file) as source_file_fd:
        source_file_lines = [ line for line in source_file_fd ]
        source_file_lines_count = len(source_file_lines)
        for lineNumber in range(0, source_file_lines_count):
            file_name = GetFileName(target_prefix, source_file_lines_count, lineNumber)
            WriteLineToNewFile(file_name, source_file_lines[lineNumber])
