#2. Grade Calculator

score = int(input("Enter the score of student : "))

if score>100:
    print("Please Enter valid Score")
    exit()
    
if score > 89:
    grade = "A"
elif score > 79:
    grade = "B"
elif score > 69:
    grade = "C"
elif score > 59:
    grade = "D"
else:
    grade = "F"
    
print(f"You got \"{grade}\" Grade.")