#Landon Grove
#5/21/24

import math

slices = int(input("How many slices of pizza does each person eat?\n"))

total = slices * 4
leftover = total % 8
pizzas = math.ceil(total / 8)

print("You will need a total of " + str(pizzas) + " pizzas and will have " + str(leftover) + " slices leftover.")
