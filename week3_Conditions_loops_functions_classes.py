######### comparison operators #########
from operator import ne
from symbol import for_stmt

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
    i = i+1
print(newSquares)
