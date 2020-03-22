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

# Loading Data with Pandas (popular library for Data analysis)
import pandas as pd
csv_path = 'resources/TopSellingAlbums.csv'
#dataframe = pandas.read_csv(csv_path)
dataframe = pd.read_csv(csv_path)
#print(dataframe.values)
print(dataframe.head())

#Using loc, iloc and ix
#There are three ways to select data from a data frame in Pandas: loc, iloc, and ix.

#loc is primarily label based;
# when two arguments are used, you use column headers and row indexes to select the data you want. loc can also take an integer as a row or column number.
item = dataframe.loc[0, "Album"]
print(item)

#iloc
#iloc is integer-based.
# You use column numbers and row numbers to get rows or columns at particular positions in the data frame.
item = dataframe.iloc[0, 1]
print(item)

#ix
#By default, ix looks for a label. If ix doesn't find a label, it will use an integer. This means you can select data by using either column numbers and row numbers or column headers and row names using ix.
#IMPORTANT: In Pandas version 0.20.0 and later, ix is deprecated.

#Using loc and iloc for slicing
#You can also use loc and iloc to slice data frames and assign the values to a new data frame.
newdf = dataframe.loc[0:2, "Artist":"Released"]
print(newdf.head())

newdf = dataframe.iloc[0:3, 0:3]
print(newdf.head())


#pandas: working with and saving data
tempDataFrame = dataframe[['Released']]
print(tempDataFrame.head())
print(type(tempDataFrame)) #returns DataFrame

dfAfter1973 = dataframe['Released'] >= 1980
print(dfAfter1973)
#0    False
#1     True
#2     True

newDataFrame = dataframe[dfAfter1973]
#c'est une forme de jointure ? s'écrit en une ligne: dataframe[dataframe['released'] >= 1973]
print(newDataFrame)

## export csv
newDataFrame.to_csv("resources/TopSellingAlbums_filtre.csv")
