print("Prime number checker")
num = int(input("Enter you number : "))
if num<=1:
    print(num,"is not a prime number.")
    exit()
is_Prime = True
for i in range(2,num):
    if num%i == 0:
        is_Prime = False
        break

if is_Prime:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number.")