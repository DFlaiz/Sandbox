#preperation for project 3
#by Doris Flaiz

# import os
# print(os.getcwd())            # what dirctory is the code looking at


lines = []                           # initializing a list
file = open("turing.txt")            # setting the file variable
         # open the file
for line in file:                    # read the lines in the file
    lines.append(line.strip())       # take eack line and add it to the list
file.close()                             # close file

print("First two lines:", lines[:2])          #print lines
print("Last two lines:", lines[-2:])
print("Number of lines:", len(lines))