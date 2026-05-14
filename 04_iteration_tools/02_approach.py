#Approach 2 (raw method like python will do without iteration tools.)
f = open('chai.py') # in file object f == iter(f) so we can use next()
print(f.__next__(), end='')
# import time
print(f.__next__(), end='')
# print("Chai is here")
print(f.__next__(), end='')
# username = "Satyam"
print(f.__next__(), end='')
# print(username)
print(f.__next__(), end='')
# raw method gives error of stopiteration.
#   File "D:\1 STUDY\2 Coding\Python Core\04_iteration_tools\02_approach.py", line 7, in <module>
#     print(f.__next__(), end='')
#           ~~~~~~~~~~^^
# StopIteration
