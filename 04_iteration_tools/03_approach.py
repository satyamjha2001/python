# Approach 3 Using Iteration tools (for and While)
# for
f = open('chai.py')
for line in f:
    print(line, end = '')
print('\n')
# while method
f = open('chai.py')
while True:                 #we have to handle the exception.
    line = f.readline()
    if not line: break
    print(line, end='')
    