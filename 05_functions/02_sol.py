# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a, b):
    return a * b


def parse_input(value):
    try:
        return int(value)
    except ValueError:
        return value


a = parse_input(input("Enter the first value: "))
b = parse_input(input("Enter the second value: "))

result = multiply(a, b)
print(result)
