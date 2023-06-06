#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last = abs(number) % 10

if last > 5:
    print("The string Last digit of", number, "is", last,"and is greater than 5")

elif last == 0:
    print("The string Last digit of", number, "is", last, "and is 0")

else:
    print("The string Last digit of", number, "is", last, m"and is less than 6 and not 0")
