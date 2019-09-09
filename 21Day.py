myset = {"arwa","ali","Reem","maram"}
#Remove "banana" by using the remove() method
print(len(myset))

#Remove "ali" by using the remove() method
myset.remove("ali")
print(myset)

#Remove "maram" by using the discard() method.
myset.discard("maram")
print(myset)

#Remove the last item by using the pop() method.
x =myset.pop()
print("This is item selected for deletion :",x)
print(myset)

#The clear() method empties the set.
myset.clear()
print(myset)

#Use del methed
"""
del myset
print(myset)

"""

#Using the set() constructor to make a set.
myset2 =set(("A","B","C","D"))
print(myset2)