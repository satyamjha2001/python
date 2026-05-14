print("Factorial Calculator !!")
num = int(input("Enter the number : "))
if num <0:
    print("Factorial of -ve number is not possible.")
else:    
    fact = 1
    for i in range(1,num+1):
        fact *= i
    print("Factorial of", num,"is", fact)