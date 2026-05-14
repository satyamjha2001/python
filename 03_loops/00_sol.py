#1. Counting Positive Numbers
numbers = [101, 1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0
for num in numbers:
    if num > 0:
        count += 1
print("Total positive numbers are :",count)        