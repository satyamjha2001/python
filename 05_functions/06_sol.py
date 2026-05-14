# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    # print(args)  # tuple of arguments
    # return sum(args)
    sum = 0
    for i in args:
        sum+=i
    return sum

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6))
print(sum_all(1,2,3,76,32))