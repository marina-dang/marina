'''for Loop'''
# Product = ("SIM", "VVS", "ConfigMax", "Nimbus", "ESP")
# for P in Product:
#       print(P)
#       print('----')
# print('-- P End --')

# word = ('Interesting')
# for w in word:
#       print(w)
# print('--w End --')

# for r in range(10):
#       print(r)
# print('-- r End --')    

# def factorial(n):
#       if n < 0:
#             print('Input must be a non-negative integer.')
#             # return None
#       result=1
#       for r in range(1, n+1):
#             result *= r
#       return result
#       # print(result)
#       # print('--End--')
# try:
#       user_input=int(input'Enter a non-negative number:')

import sys

your_input=input('Enter an integer:')

try:
      your_input=int(your_input)
except ValueError:
      print('Your input is not an integer')
      exit(1)

for number in range(1,10):
      result = number - your_input
      print(your_input, '-', number, '=', result)


'''###'''
'''while Loop'''
'''###'''
your_input=int(input('Enter a positive integer:'))
while your_input >0:
      print("You entered", your_input)
      your_input=int(input('Enter a positive integer:'))
      # order of line 50 and 51 can't be changed
      # otherwise you need to input twice 
      # then your input will be output.
      '''line 51 is necessary to be writtedn in the loop, otherwise the loop will run ifinitely'''

#If you don't want use line 51 in the loop, you can use "break":
your_input=int(input('Enter a positive integer:'))
while your_input >0:
      print("You entered", your_input)
      break  #This exits the loop after the first input

#If you want prompt user to input twice then end the loop, do like below:
your_input=int(input('Enter a positive integer:'))
while your_input >0:
      print("You entered", your_input)
      your_input=int(input('Enter again:'))
      break #This exits the loop after the final input
print('Thank You')

#If you want to mock login:
username=input("Input Your Username:")
print("Your Username:", username)
password=int(input("Input Your Password:"))
while password >100000:
      password=int(input("Input Your Password again to confirm:"))
      print("Welcome", username)
      break #This exits the loop after the final input

#If you want to add exception for login:
username=input("Input Your Username:")
print("Your Username:", username)
while True:
      password=int(input("Input Your Password:"))
      if password >= 100000:
            print(f"Dear {username}, welcome to Quen World") #f formats strings
            break
      else:
            print("The password is incorrect. Please try again")


'''continue Statement with for loop'''
for number in range(6):
      if number == 4:
            break
      print(number)
#Output is 0 1 2 3


for number in range(6):
      if number == 4:
            continue
      print(number)
#Output is 0 1 2 3 5 
