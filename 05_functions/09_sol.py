# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def fact(num):
    if num == 0:
        return 1
    return num*fact(num-1)

num = int(input("Enter a number  to calculate factorial."))
print(fact(5))