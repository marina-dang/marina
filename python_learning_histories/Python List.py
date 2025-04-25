''''Python List'''
# There are many built-in types in Pthon that allow us to group and store multiple items.
# Python lists are the most versatile among them.
# For example, we can use a Python list to store a playlist of songs so that we can easily add/remove/update songs as needed.
'''''Create a Python List'''
courses=["English","Math","Chinese","Physics"]
print(courses)
# Output: ['English', 'Math', 'Chinese', 'Physics']

courses=("English","Math","Chinese","Physics")
print(courses)
# Output: ('English', 'Math', 'Chinese', 'Physics')

'''List items of different types'''
different_types=[120, "String", 'Name']
print(different_types)
# Output: [120, 'String', 'Name']

'''create an empty list'''
empty_list=[]
print(empty_list)
# Output:[]

'''Using list() function to concert other iterables to a list'''
# int is not iterable
iterables="1234567"
result=list(iterables)
print(result)
# Output: ['1', '2', '3', '4', '5', '6', '7']

'''Access List Elements'''
#Each element in a list is associated with a number, known as an index.
#The index of first item is 0, second is 1, and so on.
languages=['English',"Spanish",'Chiniese']
print(languages[0])
# Output: English

'''Negative Indexing in Python'''
# Python also supports negative indexing.
# The index of the last element is -1, the second last is -2, and so on
languages=['English',"Spanish",'Chiniese']
print(languages[-1])
# Output: Chiniese

''''Slicing of a List in Python'''
#In Python, it is possible to access a section of items from the list using the slicing operator :
list=['Charming','Warm','Sunshine','Glory','Happy']
print(list[1:3]) # Print from index 1 to index 2
# Output: ['Warm', 'Sunshine']

list=['Charming','Warm','Sunshine','Glory','Happy']
print(list[2:]) # Print from index 2 to end
# Output: ['Sunshine', 'Glory', 'Happy']

list=['Charming','Warm','Sunshine','Glory','Happy']
print(list[:]) # Print from begining 2 to end
# Output: ['Charming', 'Warm', 'Sunshine', 'Glory', 'Happy']

'''Add Elements to a Python List'''
# We use the append() method to add an element to the end of a Python list.
fruits=['Apple','Orange','Banana']
print('Original List:',fruits)
fruits.append('Pear')
print('Updated List:',fruits)
# Output: 
# #Original List: ['Apple', 'Orange', 'Banana']
# Updated List: ['Apple', 'Orange', 'Banana', 'Pear']
'''list.append() takes exactly one argument'''



'''Add Elements at the Specified Index'''
# The insert() method adds an element at the specified index.
fruits=['Apple','Orange','Banana']
print('Original List:',fruits)
fruits.insert(2,'Pear')
print('Updated List:',fruits)
# Output: 
# Original List: ['Apple', 'Orange', 'Banana']
# Updated List: ['Apple', 'Orange', 'Pear', 'Banana']

'''Add Elements to a List From Other Iterables'''
# We use the extend() method to add elements to a list from other iterables.
num=[1,3,5,7]
print('Original List:',num)
even_num=[2,4,6,8]
num.extend(even_num)
print('Updated List:',num)
# Output:
# Original List: [1, 3, 5, 7]
# Updated List: [1, 3, 5, 7, 2, 4, 6, 8]

things=['fruits','food','drink']
print('Original List:',things)
other_things=['tools','vegetable','flowers']
things.extend(other_things)
print('Extended List:',things)
# Output:
# Original List: ['fruits', 'food', 'drink']
# Extended List: ['fruits', 'food', 'drink', 'tools', 'vegetable', 'flowers']


'''Change List Items'''
# We can change the items of a list by assigning new values using the = operator.
name=['May','Mark','Lucy']
print('Original List:',name)
name[0]='Emiley'
print('Changed List:',name)
# Output:
# Original List: ['May', 'Mark', 'Lucy']
# Changed List: ['Emiley', 'Mark', 'Lucy']


'''Remove an item from a list'''
device=['Mac','HP laptop','Lenovo laptop','Dell laptop']
print('Original Devices:',device)
device.remove('HP laptop')  # fill item name instead of index
print('Remaining Devices:',device)
# Output:
# Original Devices: ['Mac', 'HP laptop', 'Lenovo laptop', 'Dell laptop']
# Remaining Devices: ['Mac', 'Lenovo laptop', 'Dell laptop']


'''Python List Length'''
# We can use the built-in len() function to find the number of elements in a list.
company=['VMware','Broadcom','MayFoundIt','Blackboard']
print('Total num of Companies:',len(company))
# Output: Total num of Companies: 4


'''Iterating through a list'''
sprint=['Sprint1','Sprint2','Sprint3']
for SP in sprint:
    print(SP)
# Output: 
# Sprint1
# Sprint2
# Sprint3

numbers=[1,2,3,4,5]
for num in numbers:
    print(num)
# Output:  
# 1
# 2
# 3
# 4
# 5


'''List Comprehension in Python'''
#List Comprehension is a concise and elegant way to create a list.
num=[n**2 for n in range(1,6)])
print(num)
# Output: [1, 4, 9, 16, 25]
# 3**2=9, 4**2=16


'''Check if an item Exists in the Python List'''
#We use the in keyward to check if an item exists in the list.
emotion=['Happy','Sad','Anger']
print('Nervous' in emotion)
print('Happy' in emotion)
# Output: 
# False
# True

'''Write a function to fiind the larget number in a list'''
def find_largest(numbers):
    if not numbers:   # Check if the list is empty
        return None 
    largest=numbers[0]  # Initialize the largest with the first element
    for num in numbers: # loop all the numbers in variable "numbers"
        if num>largest: 
            largest=num 
    return largest      # If the num is larger the the first element, assign the value of num to largest and then return the value of largest

num_list=[1,2,9,4,5]
result=find_largest(num_list)
print('The largest number is:',result)
# Output: The largest number is: 9