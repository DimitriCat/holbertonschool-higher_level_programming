#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print ('Last digit of {:d} is'.format(number), end=" ")
if number < 0:
    number = number * -1
    digit = number % 10 * -1
    number = number * -1
else:
    digit = number % 10
if digit > 5:
    print (digit, 'and is greater than 5')
elif digit == 0:
    print (digit, 'and is 0')
elif digit < 6 and digit != 0:
    print (digit, 'is less than 6 and not 0')
