# for vs while to output same results
num = (3,4,5,6)
for i in num:
    print(i)
print('for loop ends')

num2 = 3
while num2 < 7:
    print(num2)
    num2 += 1
print('while loop ends')

# introduce "break" to stop a loop
num3 = 3
while num3 < 7:
    print(num3)
    if num3 == 4:
        break
    num3 += 1
print('while loop ends on 4')

# introduce "continue" to skip a loop
# to skip 5
num4 = 2
while num4 < 7:
    num4 += 1
    if num4 == 5:
        continue
    print(num4)
print('while loop without 5')
# the order within while is important

# issue in below loop: 
# num4 = 4 > print(num4) > output is 2
# then execute num4 += 1, now num is 3
# then go back to print(num4) > output is 3, not match if condition
# then execute num4 += 1, now num4 is 4
# then execute print(num4) > outpu is 4, not match if conditioin
# then execute num4 += 1
# then execute print(num4) > output is 5, match if condition
# once if conditions matches, num4 += 1 will not run
# then loop back to top to print(num4) > output is 5, match if condition
# then loop back to top to print(num4) > output is 5, match if condition
# ...endless
num4 = 2
while num4 < 7:
    print(num4)
    if num4 == 5:
        continue
    num4 += 1


    
    