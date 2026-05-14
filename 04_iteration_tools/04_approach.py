myList = [1,2,3,4]
I = iter(myList)
print(I)
# <list_iterator object at 0x0000027195CB05B0>
print(I.__next__())
#1
print(I)
# <list_iterator object at 0x0000027195CB05B0>  address is same
print(I.__next__())
#2
print(next(I))
#3
print(next(I))
#4
print(next(I))
# Traceback (most recent call last):
#   File "D:\1 STUDY\2 Coding\Python Core\04_iteration_tools\04_approach.py", line 15, in <module>
#     print(next(I))
#           ~~~~^^^
# StopIteration
