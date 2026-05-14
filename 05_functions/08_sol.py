# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

# normal approach

def even_generator(limit):
    for i in range(2, limit+1, 2):
        print(i)
        
# even_generator(10)

# but with return 

def even_generators(limit):
    li = []
    for i in range(2, limit+1, 2):
        # return i  # this returns only first number and function stop
        li.append(i)
    return li
# print(even_generators(10))  # outputs only 2 when return i is there
# print(even_generators(10))  # outputs list [2,4,6,8,10]

# but we want only numbers to return not in list or tuple, so we have to do loop like below.
# for i in even_generators(10):
    # print(i)
    
#To solve these above problems which we observe we can use yield
#yield means that it returns the output like 2 but it will preserve the state in memory and start from there.

def even_gen_num(limit):
    for i in range(2, limit+1, 2):
        yield i
        
# print(even_gen_num(10))
# <generator object even_gen_num at 0x73ded7813220>

for i in even_gen_num(10):
    print(i, end = ' ')
print('\n')