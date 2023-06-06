#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Fin = (number) % 10

if Fin > 5:
    print(f"Last digit of {number} is {Fin} and is greater than 5")

elif Fin <6 and Fin != 0:
    print(f"Last digit of {number} is {Fin} and is 0")

else:
    print(f"Last digit of {number} is {Fin} and is less than 6 and not 0")
