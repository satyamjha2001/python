#5. Transportation Mode Selection

distance = float(input("Enter the distance in km : "))
if distance<=0:
    print("Please enter a valid distance")
    exit()

if distance < 3:
    mode_of_transportation = "Walk"
elif distance <=15:
    mode_of_transportation = "Bike"
else:
    mode_of_transportation = "Car"
    
print("Mode of transportation is by",mode_of_transportation)