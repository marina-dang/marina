'''Python Sets'''
# A set is a collection of unique data
# Elements within a set cannot be duplicated

'''Create a Set in Python'''
# In Python, we create sets by placing all the elements inside curly braces {}
# Elements within a set are seperated by commas
userid={'m234','d854','w239','r109'}
print('UserID:',userid)
# Output: UserID: {'r109', 'w239', 'd854', 'm234'}

'''Create an Empty Set in Python'''
empty_set=set()
print('Data Type:',type(empty_set))
print('Empty Set:',empty_set)
# Output: 
# Data Type: <class 'set'>
# Empty Set: set()

'''Create a Set containing duplicates'''
dup_set={1,2,3,43,2,1}
print(dup_set)
# Output: {1, 2, 3, 43}

'''Add Set Items'''
num_set={22,33,44,55}
print('Initial Set:',num_set)
num_set.add(66)
print('Updated Set:',num_set)
# Output:
# Initial Set: {33, 44, 22, 55}
# Updated Set: {33, 66, 44, 22, 55}
'''Note: add one data once'''
'''Items in a set have no particular order'''

'''Update Python Set with another collection type'''
'''Add all items in a list into a set'''
poet1={'Meng Haoran','Wang Wei','Huang Tingjian'}
print('Poet1 Type:',type(poet1))
poet2=['Su Shi','Ou Yangxiu','Wang Anshi']
print('Poet2 Type:',type(poet2))
poet1.update(poet2)
print('Updated Poet1:',poet1)
# Output:
# Poet1 Type: <class 'set'>
# Poet2 Type: <class 'list'>
# Updated Poet1: {'Wang Anshi', 'Ou Yangxiu', 'Su Shi', 'Wang Wei', 'Meng Haoran', 'Huang Tingjian'}


'''Remove an element from a set'''
set22={45,43,54,67}
print('Original set22:',set22)
print('set22 Type:',type(set22))
set22.discard(45)
print('Updated set22:',set22)
# Output:
# Original set22: {43, 67, 45, 54}
# set22 Type: <class 'set'>
# Updated set22: {43, 67, 54}

'''Sum of all elements in a set'''
set_to_sum={99,33,-3}
print('SUM of set_to_sum:',sum(set_to_sum))
# Output:
# SUM of set_to_sum: 129
'''Note: sum only works among int numbers'''

'''Length of a set'''
things={'Fruits',44,-9,0.43,'you & me'}
print('Things Len:',len(things))
# Output:
# Things Len: 5

things={44,-9,0.43}
print('Sorted things:',sorted(things))
# Output:
# Sorted things: [-9, 0.43, 44]
things={'Fruits','ok','行','you & me'}
print('Sorted things:',sorted(things))
# Output:
# Sorted things: ['Fruits', 'ok', 'you & me', '行']
'''Note: sorted method is not supported between int and str'''

things={'Fruits',44,-9,0.43,'you & me'}
print('Things all:',all(things))
# Output:
# Things all: True

things=set()
print('Things all:',all(things))
# Output:
# Things all: True

things={0,'Fruits',44,-9,0.43,'you & me'}
print('Things all:',all(things))
# Output:
# Things all: False
'''If a set contains '0' or 'None', returns False'''

'''Set Union'''
A={1,2,3}
B={4,5,6}
C={1,5,7}
print('Union A,B,C:',A|B|C)
# Output:
# Union A,B,C: {1, 2, 3, 4, 5, 6, 7}
'''Set Intersectioin'''
A={1,2,7}
B={1,5,6}
C={1,5,7}
print('A,B,C intersection:',A&B&C)
# Output:
# A,B,C intersection: {1}


A={1,2,7}
B={1,5,6}
C={1,5,7}
print('A,B,C differ:',A-B-C)
# Output:
# A,B,C differ: {2}
# the output shows A's items that are not included in B and C



