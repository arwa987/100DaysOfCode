mylist =["AR","BR","CR","DR"]
print(mylist)
#Use append methoed
mylist.append("ER")
print("This is list after add ER :",mylist)

#use count methed
x =mylist.count("BR")
print("The name BR exists",x,"in the list")

#use insert methed
mylist.insert(0,"SA")
print("This is list after add SR in index 0 ",mylist)

#use pop methed
mylist.pop(2)
print("This is list after delete itmes in index 2 :")

#Check if "python" is present in the tuple.
tuple =("java","python","swift")

if "python" in tuple:
    print("yes python in tuple ")
