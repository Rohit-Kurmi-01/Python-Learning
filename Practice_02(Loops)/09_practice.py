items = ["apple", "banana", "orange", "apple", "mango"]

Uniqe_Item = set()

for item in items:
    if item in Uniqe_Item:
        print("Duplicate: ",item)
        break
    Uniqe_Item.add(item)

