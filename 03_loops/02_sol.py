#3. Multiplication Table Printer
num = int(input("Enter your number : "))

for i in range(1,11):
    if i == 5:  #to skip the 5th iteration
        continue
    print(num,"*",i,"=",num*i)
