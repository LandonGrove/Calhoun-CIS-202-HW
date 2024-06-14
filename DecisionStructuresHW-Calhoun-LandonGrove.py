#Landon Grove
#6/5/24

def timeSaved(speedLimit, speedTraveling, distance):
    minutes = 60
    timeIfLimit = (distance / speedLimit) * minutes #Travel time in minutes of speed limit
    timeIfUserSpeed = (distance / speedTraveling) * minutes #Travel time in minutes of user's speed
    if timeIfLimit > timeIfUserSpeed:
        print("You are saving " + str(timeIfLimit - timeIfUserSpeed) + " minutes by traveling " + str(speedTraveling - speedLimit) + "mph above the speed limit.")
    elif timeIfLimit == timeIfUserSpeed:
        print("You are traveling at the speed limit, you are not saving or losing any time.")
    else:
        print("You could save " + str(timeIfUserSpeed - timeIfLimit) + " minutes if you traveled at the speed limit.")

limit = int(input("What is the speed limit on this road, in miles per hour. Please enter a number.\n"))
avgSpeed = int(input("What is your average speed, in miles per hours. Please enter a number.\n"))
distTraveled = int(input("How far have you traveled, in miles. Please enter a number.\n"))

timeSaved(limit, avgSpeed, distTraveled)
