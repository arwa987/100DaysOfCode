
def my_function (num):
    for x in num:
        print(x)


list= [33,44,55]
my_function(list)

print("----------function2-----------------------")
def mult (num2):
    return 2*num2

print(mult(4))
print(mult(9))

print("----------function3-----------------------")
def function3(id,age,name):
    print("My name is: ",name)


function3(name="Arwa",id=123,age=20)

print("----------function4-----------------------")
def function4(*name):
    print(" my name is :",name[2])


function4("Arwa","Asma","reem ")

print("----------function5-----------------------")
def function5 (x):
    if(x>0):
        result = x+function5(x-1)
        print(result)
    else:
        result = 0
    return result


print("Rusults is ")
function5(6)