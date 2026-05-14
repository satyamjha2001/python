#05 We observe the file object and other iterable objects like list.


#List
myNewList = [1,2,3,4,5]
print(iter(myNewList) is myNewList)
#False

#File
f = open('chai.py')
print(iter(f) is f)
#True
print(iter(f) is f.__iter__())
#True