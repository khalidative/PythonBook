#====================================================================
# Program to print the contents of a  user provided file
#====================================================================

filepath = input("which file: ") # Ask the user for a file path

fileObj = open(filepath, 'r')    # open the requsted file 
                                 # in read access mode

EOF_Flag = 0                     # This file can be used to know
                                 # if the end of the files has been 
                                 # reached

while EOF_Flag != 1:             # print each line of the file
    nextLine = fileObj.readline()
    if nextLine != "":
        print(nextLine)
    else:
        EOF_Flag = 1

fileObj.close()                  # close the file
