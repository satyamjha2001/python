string = input("Enter your string : ")
for char in string:
    if string.count(char) == 1:
        print("First non-repeated character is", char)
        break

