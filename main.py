print("Select Your Ride")
print("1.Bike 2.Car")
a = int(input("Eter your choice 1/2"))
if (a == 1):
    print("What type of bike")
    print("Select Your Ride")
    print("1.Scooter 2.Motorbike")
    b = int(input("Eter your choice 1/2"))
    if (b == 1):
        print("You have selected scooter")
    else:
        print("You have selected Motorbike")
elif (a == 2):
    print("What type of car")
    print("Select Your Ride")
    print("1.SUV 2.Honda")
    b = int(input("Eter your choice 1/2"))
    if (b == 1):
        print("You have selected SUV")
    else:
        print("You have selected Honda")
else:
    print("invaliid choice")
    
