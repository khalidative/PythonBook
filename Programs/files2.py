#====================================================================
# Program to print the contents of a  user provided file
#====================================================================

filepath = input("which file: ") # Ask the user for a file path

fileObj = open(filepath, 'r')    # open the requsted file 
                                 # in read access mode

lines = fileObj.readlines()      # Read all lines in the file.
                                 # returns a list of strings
                                
fileObj.close()                  # close the file

for line in lines:               # print elements of the "lines" list
    print(line)