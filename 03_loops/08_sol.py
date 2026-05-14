items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item not in unique_item:
        unique_item.add(item)
    else:
        print("Duplicate item is", item)
        exit()
    
print("list is unique !!")