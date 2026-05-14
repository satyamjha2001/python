order_size = input("Enter the order size (Small, Medium or Large) : ")
extra_shot = input("Extra shot (y/n) : ")

if extra_shot == "y" or extra_shot == "yes":
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ", coffee)