# tuples are backed by array
from builtins import print

print("TUPLES")
F = ("You", "are", "wrong")
G = ("3",)
print(sorted(F + G))
print(F[0])
a = (1, 2, 3)
(one, two, three) = a
print(one)
print(two)

# list are backed by array
print("LISTS")
X = [1, 2, 3]
X.extend([4,5])
X.extend((44,55))
X.append([6,7])
X.append((8,9))
print(X)
print(X[0])
STRING = "Hello"
print(STRING.split(","))

#dictionary, fonctionne un peu comme une map
print("DICTIONARY")
albums={"thriller":"1982", "bodyguard":1983, "thriller":"1984"}
print(albums)
#print(albums[0]) marche pas, c pas backé par un array
print(len(albums))
print("thriller" in albums)
del(albums["thriller"])
print("thriller" in albums)
print(albums)

# sets, unordered, unique elements; methods: add, remove, blabla in mySet, & (ndlr: intersection), union, issubset,
mySet1={1,3,2,4,5,4}
mySet2={1,7, 3}
intersectionSet = mySet1 & mySet2
print(mySet1)
print(mySet2)
print(intersectionSet)
print(intersectionSet.issubset(mySet2))