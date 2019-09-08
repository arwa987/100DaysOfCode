Set ={"apple","banana","cherry"}
print(Set)

# Access Items
for a in Set:
    print(a)

#Check if "banana" is present in the set.
print("banana" in Set)

#Add an item to a set, using the add() method
Set.add("orange")
print(Set)

#Add multiple items to a set, using the update() method
Set.update(["orange","mango","grapes"])
print(Set)