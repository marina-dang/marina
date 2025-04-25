a = 33
b = 44
if a == b:
    print("a equals b")
elif a > b:
    print("a is not equal to b")
elif a >= b:
    print("a is greater than or equal to b")
elif a <= b:
    print("a is less than or equal to b")
else:
    print("a is less than b")

x = 77
y = -55
if x > y: print("x is greater than y")

w = 66
z = 0.6
print("w equals z") if w == z else print("w is not equal to z")

l = 238
m = 238
print("l is greater than m") if l > m else print("l is less than or equal to m") if l == m else print("l is not b")

q = 99
p = 88
r = 100
if q > p and p < r:
    print("q is greater than p and p is less than r")


w = 66
m = 238
r = 100
q = 99
if w < q or r > m:
    print("w is less than q or r is greater than m")
    print("w = 66, m = 238, r = 100, q = 99")


w = 66
m = 238
if not w > m: print("w is not greater than m")


w = 66
if w > 16:
    print(">16")
    if w > 33:
        print(">33")
        if w > 55:
            print(">55")
        else:
            print("<=55")
else:
    print("w <= 16")

w = 66
if w < 66:
    pass

number = 25
print('number:', number, '℃')
print('number:' + str(number) + '℃')
if number > 20:
	print('it is warm.')
else:
	print('it is cold.')
     
import random
dice = random.randint(1, 6)
print('You rolled a', str(dice))
if dice == 6:
	print('You got 6!🥳')
else:
	print('Try again!')
     
age = 16
print('Age:', age)
if age < 13:
     print('You are a child.')
elif age < 20:
    print('You are a teenager.')
else:
     print('You are an adult.')


yourAge = 19
if yourAge < 13:
     print('You are a child.')
elif yourAge < 20:
    print('You are a teenager.')
    if yourAge > 17:
         print('you are an adult.')
else:
     print('You are an adult.')

myAge = int(input('Enter your age:'))
print('Your age is', myAge)
if myAge < 13:
     print('You are a child.')
     if myAge < 5:
          print('You are a baby.')
elif myAge < 20:
     print('You are a teenager.')
     if myAge > 17:
          print('You are an adult.')
elif myAge < 60:
     print('You are an adult.')
     if myAge < 50:
            print('You are a middle-aged adult.')
            if myAge < 36:
                 print('You are a young adult.')
else:
     print('You are an older adult.')
          


