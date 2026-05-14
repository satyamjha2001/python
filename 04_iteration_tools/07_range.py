R = range(5)
print(R)
# range(0, 5)
I = iter(R)
print(I)
# <range_iterator object at 0x00000246BE08C350>
print(next(I))
# 0
print(next(I))
# 1
print(next(I))
# 2
print(next(I))
# 3
print(next(I))
# 4
print(next(I))
# Traceback (most recent call last):
#   File "D:\1 STUDY\2 Coding\Python Core\04_iteration_tools\07_range.py", line 12, in <module>
#     print(next(I))
#           ~~~~^^^
# StopIteration
