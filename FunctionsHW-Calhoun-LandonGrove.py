#Landon Grove
#6/14/24

def timeKeeping():
    print("Please enter a time in hours and minutes.")
    validHours = checkHours(int(input("Enter hours between 0 and 23.\n")))
    validMinutes = checkMinutes(int(input("Enter minutes between 0 and 59.\n")))
    if validHours == "Error: value out of range.":
        print(validHours)
    elif validMinutes == "Error: value out of range.":
        print(validMinutes)
    else:
        print("You entered " + str(validHours) + " hours  and " + str(validMinutes) + " minutes.")

def checkHours(hours):
    if hours >= 0 and hours <= 23:
        return hours
    else:
        return "Error: value out of range."

def checkMinutes(minutes):
    if minutes >= 0 and minutes <= 59:
        return minutes
    else:
        return "Error: value out of range."

timeKeeping()
