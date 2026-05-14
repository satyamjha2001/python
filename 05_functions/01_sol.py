# 2. Function with Multiple Parameters
# Problem: Create a function that takes two numbers as parameters and returns their sum.

a, b = map(int, input("Enter two numbers separated by space: ").split())
def add(a, b):
    return a+b

print(add(a,b))