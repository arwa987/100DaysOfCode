x =  {
    "name":"ali",
    "age":20,
    "years":2000
}

#Check if "phonenum" is present in the dictionary.
if "years" in x:
    print("yes, is one of the keys in x dictionary.")

#Print the number of items in the dictionary.
print(len(x))

#Adding Items
x["last name"]="alhrbi"
print(x)

#Removing Items use pop method
x.pop("years")
print(x)

#Removing Items use popitem method
x.popitem()
print(x)

#del method
del x["age"]
print(x)

#clear method
x.clear()
print(x)

del x
print(x)