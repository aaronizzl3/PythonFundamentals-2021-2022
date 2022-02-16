
# Distance = Speed x Time
# Time = Distance / Speed
# Speed = Distance / Time

option = int(input("1 - Distance\n2 - Time\n3 - Speed\nOption: "))

if option == 1:
    speed = int(input("Enter speed (mph): "))
    time = int(input("Enter time (hours): "))
    distance = speed * time
    print(f"Distance covered is {distance} miles.")
elif option == 2:
    distance = int(input("Enter distance (miles): "))
    speed = int(input("Enter speed (mph): "))
    time = distance / speed
    print(f"Time taken was {time} hours.")
elif option == 3:
    distance = int(input("Enter distance (miles): "))
    time = int(input("Enter time (hours): "))
    speed = distance / time
    print(f"Your speed was {speed}mph.")
else:
    print("Unexpected input.")