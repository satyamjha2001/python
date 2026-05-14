#7. Password Strength Checker
password = input("Enter your password : ")
if len(password) < 6:
    password_strength = "Weak"
elif len(password) < 11:
    password_strength = "Medium"
else:
    password_strength = "strong"
    
print("Your password is", password_strength)