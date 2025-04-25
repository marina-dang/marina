list1 = ["apple", "banana", "blue", "water"]
print(list1[1])
print(list1[-2])
print(list1[0])
print(list1[1:3]) # return the second, third item
print(list1[:2]) # return the first, second item
print(list1[1:]) # return from second to end
print(list1[-4:-1]) # retrun without the last one
if "blue" in list1:
    print("blue is in list1")

# change list item value
list2 = ["sea", "lake", "ocean", "river", "creek", "stream", "brook"]
list2[1] = "marina"
print(list2)
list2[1:3] = ["lake", "marina", "sunshine"]
print(list2)
list2[1:4] = ["smart"]
print(list2)
list2[1:2] = "lake"
print(list2)
list2.insert(1, "marina")
print(list2)
list2.append("flow")
print(list2)

# add item from one list into another
list3 = ["rainbow", "rain"]
list4 = ["peace", "harmony"]
list3.extend(list4) # add list4 into list3
print(list3)

# add tuple into list, remove list item
list5 = ["gentle", "strength"]
tuple1 = ("walk", "casual")
list5.extend(tuple1)
print(list5)
list5.remove("walk")
print(list5)
list5.pop(1) # remove the second item
print(list5)
# del list5
# print(list5)
list5.clear()
print(list5)

# print list items one by one
list6 = ["rose", "lotus", "orchid"]
for flower in list6:
    print(flower)

list7 = ["2", "4", "6"]   
print(len(list7))
print(range(len(list7)))

for i in range(len(list7)):
    print(list7[i])


list8 = ["three","six","nine"]
i = 0
while i < len(list8):
    print(list8[i])
    i = i+1

list10 = ["溪流","清风", "明月", "白云"]
[print(i) for i in list10]

# sort list
list11 = ["Obsidian","aquamarine", "rutilated quartz", "phamant quartz"]
list11.sort()
print(list11)
list11.sort(reverse=True)
print(list11)

list11.sort(key=str.lower)
print(list11)
list11.sort(reverse=True, key=str.lower)
print(list11)

list12 = [3,6,9]
listcopy = list12.copy()
print(listcopy)

list13 = ["rose", "mayflower", "lotus"]
print("rose" in list13)




