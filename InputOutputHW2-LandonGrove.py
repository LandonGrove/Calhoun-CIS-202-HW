#Landon Grove
#5/21/24

import math

slices1 = int(input("How many slices of pizza does the first person eat?\n"))
slices2 = int(input("How many slices of pizza does the second person eat?\n"))
slices3 = int(input("How many slices of pizza does the third person eat?\n"))
slices4 = int(input("How many slices of pizza does the fourth person eat?\n"))

TotalSlices = slices1 + slices2 + slices3 + slices4
leftover = TotalSlices % 8
pizzas = math.ceil(TotalSlices / 8)

print("You will need a total of " + str(pizzas) + " pizzas and will have " + str(leftover) + " slices leftover.")
