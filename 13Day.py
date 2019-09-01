numbers =[1.3,4.8 ,7.7,9.3]
print(numbers)

print("the items in index 3 is:")
print(numbers[3])

print("all items in list ")
for a in numbers :
    print(a)

# Change Item Value
numbers [0] = 2.4
print("After modification")
print(numbers)

#remove item
del numbers[3]
print("After remove")
print(numbers)