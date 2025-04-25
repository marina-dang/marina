set1 = {"cloud", "river", "rain", "cloud"}
print(set1)

set2 = {True, 1, "raindrop"}
print(set2)

set3 = {0, False, "rainbow", 2.5, -1, 2.5, "rainbow"}
print(set3)
print(len(set3))
print(type(set3))
print("rainbow" in set3)

set4 = set(["blue", "black"])
print(type(set4))
print(set4)
print("rainbow" not in set4)
set4.add("rainbow")
print(set4)

set5 = {"april", "winter", "autum"}
set6 = {1,2,3}
set6.update(set5)
print(set6) # set6 is changed

set7 = {"april", "winter", "autum"}
set8 = {1,2,3}
set8.union(set7)
print(set8)  # set8 is not changed

set9 = {"april", "winter", "autum"}
set9.remove("april")
print(set9)
set9.discard("april")
print(set9)
set9.pop() # be careful to use .pop()
print(set9)
set9.clear()
print(set9)
del set9
# print(set9) # error: set9 is not defined

set10 = {"blue", "22", "23"}
for x in set10:
    print(x)

set11 = {"rose", 22, 23.5}
set12 = {"0", -16, "jack15"}
set13 = set11 | set12
print(set13)
set14 = set10.union(set11, set12, set13)
print(set14)
set15 = set8 | set10 | set12
print(set15)

set16 = {"x", "y", -11,2}
tuple1 = ("river", 16, True)
settuple = set16.union(tuple1)
print(settuple)
# tupleset = tuple1.union(set16)
# print(tupleset)

set17 = {16, 1.6, "black"}
set18 = {"rain", -1}
set17.update(set18)
print(set17) # changed
print(set18) # no change
set19 = set17.intersection(set18) # extract the items existing both in set17 and set18
print(set19)
set20 = set17 & set18
print(set20)

set21 = {"black", 16, -22, True, 1}
tuple2 = (True, 2.4, 16, 1)
list1 = ["blue", 0, False, 16, True, 1]
settuplelist = set21.intersection(tuple2,list1)
print(settuplelist)
set21.intersection_update(tuple2, list1)
print(set21) # changed

set22 = set17.difference(set21)
print(set22) # extract items only existing in set17
set22 = set17 - set21
print(set22)
print(set17)
set17.difference_update(set21)
print(set17) # changed

set23 = {16, True, "blue", 2.3}
set24 = {16, False, "black", -1}
set25 = set23.symmetric_difference(set24)
print(set25)
set26 = set23 ^ set24
print(set26)
print(set23) # no change
set23.symmetric_difference_update(set24)
print(set23) # changed

set27 = {1, 2, 3}
set28 = set27.copy()
print(set28)
print(set27)













