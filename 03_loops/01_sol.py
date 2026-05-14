#Sum of Even Numbers
num = int(input("Enter your number : "))
sum = 0
for i in range(num+1):
    if i%2 == 0:
       sum+=i

print("Sum of even numbers upto",num,"is",sum) 