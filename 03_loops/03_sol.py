#4. Reverse a String

string = input("Enter your string : ").strip()
rev_string=""
# for i in range(len(string)-1,-1,-1):
    # rev_string+=string[i]
    #OR
for char in string:
    rev_string = char + rev_string  #char pehle then rev_string ulta print karega. 
print(rev_string)