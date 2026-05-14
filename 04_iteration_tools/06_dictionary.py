#06 iter over Dictionary

d = {'a': 1, 'b':2}
for key in d.keys():
    print(key)
#a
#b

I = iter(d)
print(I)
# <dict_keyiterator object at 0x000001E5F8CC0040>
print(next(I))
# a
print(next(I))
# b
print(next(I))
# Traceback (most recent call last):
#   File "D:\1 STUDY\2 Coding\Python Core\04_iteration_tools\06_dictionary.py", line 16, in <module>
#     print(next(I))
#           ~~~~^^^
# StopIteration