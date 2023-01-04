#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = abs(number) % 10
if number < 0:
    rem = -rem
print(f"Last digit of {number:d} is {rem:d} and is", end=" ")
if rem > 5:
    print("greater than 5")
if rem < 6 and rem != 0:
    print("less than 6 and not 0")
elif rem == 0:
    print("0")
