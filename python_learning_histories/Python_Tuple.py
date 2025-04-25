'''Python Tuple'''
# Ptyon Tuple is a collection similar to List.
# Difference is that items in a tuple immutable.

'''Create a Python Tuple'''
#We create a tuple by placing items inside parentheses ()
tuple_num=(1,2,3.4,-2,0,2)
print(tuple_num)
# Output: (1, 2, 3.4, -2, 0, 2)

tuple_str=('Sun','Cloud','Star','Moon')
print(tuple_str)
# Output: ('Sun','Cloud','Star','Moon')

'''Create a Tuple using tuple() constructor'''
tuple_constructor=tuple()
print(tuple_constructor)
# Output: ()

tuple_constructor_num=tuple((1,2,3.4,-2,0,2))
print(tuple_constructor_num)
# Output: (1, 2, 3.4, -2, 0, 2)

tuple_constructor_str=tuple(('Sun','Cloud','Star','Moon'))
print(tuple_constructor_str)
# Output: ('Sun','Cloud','Star','Moon')

'''Different Types of Python Tuples'''
'''Empty Tuple'''
empty_tuple=()
print(empty_tuple)

'''Access Items Using Index'''
tuple_index=('Mon','Tue','Wed','Thu','Fri')
print(tuple_index[1:4])
# Output: ('Tue', 'Wed', 'Thu')

'''Tuple cannot be modified'''
tuple_modify=('Dark','Dawn')
tuple_modify[1]='Bright'
print(tuple_modify)
# Output: ERROR!
# TypeError: 'tuple' object does not support item assignment

'''Python Tuple Length'''
'''Python Tuple Allows Duplicates'''
tuple_num_length=(1,2,3.4,-2,0,2)
print('Total Items:',len(tuple_length))
# Output: Total Items: 6

tuple_str_length=('Sun','Cloud','Star','Moon','Sun')
print('Total Items:',len(tuple_str_length))
# Output: Total Items: 5

'''Iterate through a Tuple'''
tuple_iterate=('Sun','Cloud','Star','Moon','Sun')
for item in tuple_iterate:
    print(item)
# Output: 
# Sun
# Cloud
# Star
# Moon
# Sun

tuple_exponentation=(n**2)


'''Delete Tuples'''
#We cannot delete individual items of a tuple.
#However, we can delete the tuple itself using the del statement.
emotion=('Sad','Happy','Angry','Scared')
characteristics=('Resilence','Strong mind','Brief')
del emotion
print(emotion,characteristics)


'''Challenge'''
'''Write a function to modify a tuple by adding an element at the end of it'''
#For inputs with tuple (1,2,3) and element 4, the return value should be (1,2,3,4)
#Hint: You need to first convert the tuple to another data type, such as a list.
def modify_tuple():
    convert_to_list=list[modify_tuple]
    convert_to_list.append(4)
print(convert_to_list)
# Output: Error!

def modify_tuple():
    tuple_to_convert=(1,2,3)    
    convert_to_list=list(tuple_to_convert)
    convert_to_list.append(4)
    return convert_to_list
modified_list=modify_tuple()
print(modified_list)
# Output: (1, 2, 3, 4)

'''Add an elem into a tuple without a function'''
tuple_change=(1,2,3)
list_convertion=list(tuple_change)
list_convertion.append(4)
modified_tuple=tuple(list_convertion)
print(modified_tuple)
# Output: (1, 2, 3, 4)

















