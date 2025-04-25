tuple1 = ("blue")
print(type(tuple1))

tuple1 = ("blue",)
print(type(tuple1))

tuple2 = ("blue", "green", "black")
tuple3 = (1, 2, 3, 4, 5, 6)
tuple4 = (True, False, True)
tuple5 = (1, True, "stream", 2.4, -7, "blue16")
print(tuple2, tuple3, tuple4, tuple5)
print(type(tuple2))
print(tuple2[0])
tuple6 = (tuple5)
print(type(tuple6))
print(tuple6)
print(tuple6[-1])
print(tuple6[:4])
print(tuple6[-4:-1])
if "blue16" in tuple6:
    print("blue16 is in tuple6")

tuple7 = (6, "blue", 2.6, -1, True)
listconvert = list(tuple7)
print(type(listconvert))
print(listconvert)
listconvert[2] = "2.6"
print(listconvert)
tuple7 = tuple(listconvert)
print(type(tuple7))
print(tuple7)

listconvert = list(tuple7)
print(type(listconvert))
print(listconvert)
listconvert.append("black")
print(listconvert)
tuple7 = tuple(listconvert)
print(type(tuple7))
print(tuple7)

tuple8 = (9, False, "sky")
tuple7 = tuple7 + tuple8
print(tuple7)

listconvert = list(tuple7)
listconvert.remove(False)
print(listconvert)
tuple7 = tuple(listconvert)
print(tuple7)
print(tuple8)
# del tuple8
# print(tuple8)
print(tuple7)


tuple9 = ("good","better","best")
print(len(tuple9))

for l in tuple9:
    print(l)

i = 1
while i < len(tuple9):
    print(tuple9[i])
    i = i + 1

tuplemultiply = tuple9 * 2
print(tuplemultiply)

print(tuple9.count("good"))
print(tuple9.index("good"))

weekday = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
(x, y, *z) = weekday
print(z)
print("Mon" in weekday)