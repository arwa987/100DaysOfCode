TEP =("arwa","ali","asma","ahmad")

#Check if "arwa" and "sultan "is present in the tuple.
if "arwa" in TEP:
    print("yes arwa is in tuple ")
if "sultan" in TEP:
    print("yes sultan is in tuple ")

# Repeat Item
TEP2 =("اروى",)*4
print(TEP2)

""" 
TEP2 =("asma")*3
print(TEP2)
"""

x =(3,4,5,6)
x = x + (1,2,3)
print(x)

#Tuple Length
print("The length of tuple TEP is :")
print(len(TEP))
print(TEP)

# بناء tuple /صف
TEP3 =((3,4,5,6,"A","B"))
teple4 =tuple(TEP3)
print("New tuple :")
print(teple4)


#count methed
""" 
ترجع عدد صحيح كم مرة تم ايجاد عنصر عنده نفس القيمة 
التي مررناها لها مكان البارميتر 
"""
C = TEP.count("asma")
print('name asma exists',C ,'in the tuple')
v =TEP2.count("اروى")
print('name اروى exists',v,'in the tuple')


#index methed
"""
ترجع index الموجود في القيمة التي مررناها 
"""
print(TEP.index("arwa"))
