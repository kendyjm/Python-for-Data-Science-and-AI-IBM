# Reading Files with Open
import matplotlib as matplotlib

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
# dataframe = pandas.read_csv(csv_path)
dataframe = pd.read_csv(csv_path)
# print(dataframe.values)
print(dataframe.head())

# Using loc, iloc and ix
# There are three ways to select data from a data frame in Pandas: loc, iloc, and ix.

# loc is primarily label based;
# when two arguments are used, you use column headers and row indexes to select the data you want. loc can also take an integer as a row or column number.
item = dataframe.loc[0, "Album"]
print(item)

# iloc
# iloc is integer-based.
# You use column numbers and row numbers to get rows or columns at particular positions in the data frame.
item = dataframe.iloc[0, 1]
print(item)

# ix
# By default, ix looks for a label. If ix doesn't find a label, it will use an integer. This means you can select data by using either column numbers and row numbers or column headers and row names using ix.
# IMPORTANT: In Pandas version 0.20.0 and later, ix is deprecated.

# Using loc and iloc for slicing
# You can also use loc and iloc to slice data frames and assign the values to a new data frame.
newdf = dataframe.loc[0:2, "Artist":"Released"]
print(newdf.head())

newdf = dataframe.iloc[0:3, 0:3]
print(newdf.head())

# pandas: working with and saving data
tempDataFrame = dataframe[['Released']]
print(tempDataFrame.head())
print(type(tempDataFrame))  # returns DataFrame

dfAfter1973 = dataframe['Released'] >= 1980
print(dfAfter1973)
# 0    False
# 1     True
# 2     True

newDataFrame = dataframe[dfAfter1973]
# c'est une forme de jointure ? s'écrit en une ligne: dataframe[dataframe['released'] >= 1973]
print(newDataFrame)

## export csv
newDataFrame.to_csv("resources/TopSellingAlbums_filtre.csv")

# NUMPY
# Import the libraries
import time
import sys
import numpy as np

import matplotlib.pyplot as plt


# Plotting functions
def Plotvec1(u, z, v):
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


def Plotvec2(a, b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


# Create a numpy array
a = ["0", 1, "two", "3", 4]
a = np.array([0, 1, 2, 3, 4])
# Check the type of the array
# Check the type of the values stored in numpy array
print(a, type(a), a.dtype)

# Create a numpy array
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
# Check the type of the array
# Check the type of the values stored in numpy array
print(b, type(b), b.dtype)

##NUMPY Assign value
c = np.array([20, 1, 2, 3, 4])
c[0] = 100
c[4] = 0
print(c)  # [100,1,2,3,0]

##NUMPY Slicing
# Slicing the numpy array
d = c[1:4]
print(d)  # [1,2,3]
# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
print(c)  # [100,1,2,300,400]

# Assign Value with List
# Create the index list
select = [0, 2, 3]
# Use List to select elements
d = c[select]
print(d)  # [100,2,300]
# Assign the specified elements to new value
c[select] = 100000
print(c)  # [100000,1,100000,100000,400]

# Other Attributes
# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
# The attribute size is the number of elements in the array
# Get the number of dimensions of numpy array with ndim
# The attribute shape is a tuple of integers indicating the size of the array in each dimension:
print(a, a.size, a.ndim, a.shape)

# Create a numpy array
a = np.array([1, -1, 1, -1])
# Get the mean of numpy array
mean = a.mean()
print(a, mean)

# Get the standard deviation (ecart-type) of numpy array
standard_deviation = a.std()
print(standard_deviation)

# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])
# Get the biggest value in the numpy array
# Get the smallest value in the numpy array
print(b, b.max(), b.min())

# Numpy Array Operations
## Array Addition
u = np.array([1, 0])
v = np.array([0, 1])
z = u + v
print("u=" + str(u), "v=" + str(v), "u+v=" + str(z))
# Plot numpy arrays
Plotvec1(u, z, v)

## Array Multiplication
# Create a numpy array
y = np.array([1, 2])
# Numpy Array Multiplication
z = 2 * y
print(y, z)

# Product of Two Numpy Arrays
# Create two numpy array
u = np.array([1, 2])
v = np.array([3, 2])
# Calculate the production of two numpy arrays
z = u * v
print(u, v, "produit de 2 numy apparays=", z)

# Calculate the dot product
print(u, v, "produit scalaire=", np.dot(u, v))

# Adding Constant to a Numpy Array
u = np.array([1, 2, 3, -1])
v = u + 1
print(u, v)

# Mathematical Functions
## The value of pie
print(np.pi)

# We can apply the function sin to the array x and assign the values to the array y; this applies the sine function to each element in the array:
# Create the numpy array in radians
x = np.array([0, np.pi / 2, np.pi])
y = np.sin(x)
print(x, y)

# Linspace¶
# A useful function for plotting mathematical functions is "linespace".
# Linespace returns evenly spaced numbers over a specified interval.
# We specify the starting point of the sequence and the ending point of the sequence.
# The parameter "num" indicates the Number of samples to generate, in this case 5:
z = np.linspace(-5, 5, 10)
print("linspace(-5,5,10)", z)

# Makeup a numpy array within [0, 2π] and 100 elements
x = np.linspace(0, 2 * np.pi, num=100)
# Calculate the sine of x list
y = np.sin(x)
print(x, y)
# Plot the result
plt.plot(x, y)

#Two Dimensional Numpy
## Calculate the dot product, produit matriciel
a = np.array([[0,1,1], [1,0,1]])
b = np.array([[1,1], [1,1], [-1,1]])
c = np.dot(a, b)
d= a*b
print("a=", a, "b=", b, "c=", c, "d=", d)
print("shape a=", np.shape(a))
print("shape b=", np.shape(b))
print("shape c=", np.shape(c))

# Import the libraries
import numpy as np
import matplotlib.pyplot as plt

# Create a list
a = [[11, 12, 13, 5], [21, 22, 23, 5], [31, 32, 33, 5]]

# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
# Show the numpy array dimensions -> 2
# Show the numpy array shape -> (3, 4)
# Show the numpy array size -> 12 elements
print(A, A.ndim, A.shape, A.size)

# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
# Get the transposed of C
print(C, C.T)

X=np.array([[1,0,1],[2,2,2]])
out=X[0,1:5]
print(out)