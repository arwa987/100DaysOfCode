for a in range(9):
    print(a)

#Using the start parameter
print("----------------------------------")
for a in range(4,9):
    print(a)

#Increment the sequence with 2(default is 1)
print("----------------------------------")
for a in range(2,9,3):
    print(a)

#Else in For Loop
print("----------------------------------")
for a in range(9):
    print(a)
else:
    print("the end :)")


#Nested Loop
print("----------------------------------")
name =["reem","sara","asma"]
id =[123,345,678]
for f in name:
    for i in id:
        print(f,i)