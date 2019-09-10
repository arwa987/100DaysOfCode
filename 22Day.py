me = {
    "NAME":"arwa",
    "AGE":22,
    "ID":1234
}
print(me)
a =me["AGE"]
print(a)

# use get
b =me.get("NAME")
print(b)

#Change the "ID" to 456
me["ID"] = 456
print(me)

#Print all key names in the dictionary, one by one.
for x in me:
    print(x)

#Print all values in the dictionary, one by one
for y in me:
    print(me[y])


# use values and for
for z in me.values():
    print(z)


# use value
me2 ={"NAME":"aml","AGE":33,"ID":999}
print(me2.values())

#Loop through both keys and values, by using the items() function.
for a,b in me2.items():
    print(a,b)

#print all items without for
print(me2.items())