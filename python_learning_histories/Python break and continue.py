'''Python break and continue'''
# break: exists the loop entirely
# continue: skips the current interation and proceeds to the nest one.
'''Python break Statement'''

#output 0~6 in range(10)
for number in range(10):
    if number ==6:
        break
    print(number)

#output 0~6 in range(10)
number=0
while number < 10:
    print(number)
    if number ==6:
        break
    number += 1
