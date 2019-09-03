letter = ["A","B","C","D","E"]
print("The number of items in list is :")
print(len(letter))

#add items
letter.append("F")
print("After add item in list ")
print(letter)

#add an item at the specified index
letter.insert(0,"AR")
print("Add AR in index 0")
print(letter)

#remove methoed
letter.remove("B")
print("After remove B")
print(letter)

#pop methed
print("Use pop methed :")
letter.pop()
print(letter)
letter.pop(3)
print("removes the index(3)")
print(letter)

#لحذف القائمة
letter.clear()
print("remove all items in lis :")
print(letter)

#copy method
x =[1,2,3,4]
y =x.copy()
x.pop(1)
print("copy by copy methed :")
print(x)
print(y)

#list methed
b =[8,7,6]
c =list(b)
print("copy by list methed: ")
print(c)


#Using the list() constructor to make a list.
d = list((2,2,5,7,8))
print("new lis :")
print(d)