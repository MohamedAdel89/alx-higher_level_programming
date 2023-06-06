#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Fin = abs(number) % 10

if Fin > 5:
    print(f"Last digit of {number} is {Fin} and is greater than 5 and not 0")

elif Fin <6 and Fin != 0:
    print(f"Last digit of {number} is {Fin} and is less than 6 and not 0")    

else:
    print(f"Last digit of {number} is {Fin} and is 0")


# elif last_digit == 0:
#    message = "and is 0"
# else:
#    message = "and is less than 6 and not 0"
