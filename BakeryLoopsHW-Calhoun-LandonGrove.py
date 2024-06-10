#Landon Grove
#6/8/24

def businessDay():
    muffins = 10
    cupcakes = 10
    while True:
        userBuys = input("Would you like a muffin or cupcake?\n")
        if userBuys.lower() == "cupcake":
            if cupcakes >= 1:
                print("Here is your cupcake. Thanks and have a great day!\n")
                cupcakes -= 1
            else:
                print("Apologies, but cupcakes are out of stock.\n")
        elif userBuys.lower() == "muffin":
            if muffins >= 1:
                print("Here is your muffin. Thanks and have a great day!\n")
                muffins -= 1
            else:
                print("Apologies, but muffins are out of stock.\n")
        elif userBuys.lower() == "end":
            print("The business day has ended.")
            break
        elif userBuys == str(0):
            print("muffins: " + str(muffins) + "\ncupcakes: " + str(cupcakes) + "\n")
        else:
            print("Please enter a valid input: muffin, cupcake, 0, or end.\n")

businessDay()
