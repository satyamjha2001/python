age = int(input("Enter valid age : "))
if age>0:
    day = input("Enter day name : ").strip().lower()
    if day in (
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ):
        price = 12 if age >= 18 else 8  #new method of if else like ternary in cpp
        if day == "wednesday":
            price -= 2
        print("Ticket price for you is $",price)
    else:
        print("Enter valid day name")
else:
    print("please enter valid age")
    
