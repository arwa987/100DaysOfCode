#Local Scope
def funcation():
    fname ="arwa"
    print(fname)
    def funcation2():
        print(fname)
        funcation2()


funcation()

#Global Scope
name ="Reem"
def fun3():
    print(name)

fun3()

print(name)
