# Reading Files with Open
File1 = open('Rectangle.py', 'r')
print(File1.name, File1.mode, File1.closed)
File1.close()
print(File1.name, File1.mode, File1.closed)

# 'with' auto-close the file after the process
with open('Rectangle.py', 'r') as File1:
    # read all content:
    # allContent = File1.
    # read()
    # print(allContent)

    # read a line
    # currentLine = File1.readline()
    # print(currentLine)

    # put lines in a list
    listLines = File1.readlines()
    print(listLines)

    ## PRINT CONTENT
    # 1 print(allContent)
    # 2 for line in listLines:
    #    print(line)
    # for line in File1:
    #    print(line)
print(File1.name, File1.mode, File1.closed)

# Writing Files with Open
with open('resources/test.txt', 'w') as File2:
    File2.writelines(["test", "\n", "aa"])
with open('resources/test.txt', 'r') as File2:
    print(File2.readlines())

