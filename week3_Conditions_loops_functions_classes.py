######### comparison operators #########
from operator import ne
from statistics import multimode
from symbol import for_stmt, while_stmt

a = 6
a == 7
"A" == "B"  # works also with str
# 1=2 #produces an error
6 >= 5  # True
2 != 3  # inequality test

######### branching #########
age = 17
if age > 18:
    print("you can enter")
elif age == 18:
    print("go see plink floyd")
else:
    print("go see Meat Loaf")
print("move on")

######### range, loops for, enumerate, range, while #########
N = 3
range(N)  # => sequence [0,...,N-1]

print(range(3))
print(range(10, 15))

# Write a for loop the prints out all the element between -5 and 5 using the range function.
for index in range(-5,6):
    print(index)

squares = ["red", "yellow", "green", "purple", "blue"]
print(squares)
for i in range(len(squares)):
    squares[i] = squares[i] + str(i)
print(squares)

for square in squares:
    print(square)

for index, label in enumerate(squares):
    print("index:" + str(index) + ", label:" + label)
    print(index, label)

for kv in enumerate(squares):
    print(kv)

newSquares = []
i = 0
while not (square := squares[i]).startswith("green"):
    print(f"adding {square} to newSquares")
    newSquares.append(square)
    i = i + 1
print(newSquares)


######### functions #########
def add1(a):
    """
    increment by 1\n
    :param a: my comment about 'a'
    :return: a+1
    """
    b = a + 1
    return b


c = add1(5)
print(c)
d = add1(8)
print(d)

help(add1)


def mult(a, b):
    """
    a * b
    :return:
    """
    return a * b


print(mult(2, 5))
print(mult(2.7, 5.9))
print(mult(2, "TO"))


def MJ():
    """
    no return
    """
    print("Mickael Jackson")


MJ()


def nowork():
    pass


print(nowork())


def noworkBis():
    return None


print(noworkBis())


def artistNames(*names):
    for name in names:
        print(name)


artistNames("kendy", "jm")


def pinkFloyd():
    global claimedSales
    claimedSales = "45m"
    return claimedSales


pinkFloyd()
print(claimedSales)


def hello():
    print("hello")

artist = "Michael Jackson"
def printer(artist):
    global internal_var # a way to create global variables from within a function as follows:
    internal_var= "Whitney Houston"
    print(artist,"is an artist")
printer(artist)
printer(internal_var)



##### Objects and Classes #####
# We could find out the type of an object by using the type command.
class Circle(object  # parent object
             ):
    def __init__(self, radius, color = 'white'):
        '''
        this is a constructor
        :param radius:
        :param color: has a defaut value 'white'
        '''
        self.radius = radius
        self.color = color


    def toPrint(self):
        print(self.radius, self.color)
        None


myCircle1 = Circle(1, 'red')
print(myCircle1.radius)
print(myCircle1.color)
myCircle1.toPrint()
myCircle1.color = "blue"
myCircle1.toPrint()

myCircle2 = Circle(2)
myCircle2.toPrint()

#  The dir function is useful for obtaining the list of data attributes and methods associated with a class.
#  The object you're interested in is passed as an argument.
#  The return value is a list of the objects data attributes.
#  The attribute surrounded by underscores are for internal use, and you shouldn't have to worry about them.
print(dir(Circle))