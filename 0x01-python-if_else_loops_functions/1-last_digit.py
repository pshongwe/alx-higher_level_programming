#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
if (number > 0) and (int(num[len(num) - 1]) > 5):
    print(f"Last digit of {number} is \
{num[len(num) - 1]} and is greater than 5")
elif int(num[len(num) - 1]) == 0:
    print(f"Last digit of {number} is \
{num[len(num) - 1]} and is 0")
else:
    print(f"Last digit of {number} is \
{num[len(num) - 1]} and is less than 6 and not 0")
