class Myfristclaa:
    def __init__(self,name,age):
        self.name =name
        self.age =age

    def fun(self):
        print("my name is ",self.name)


m = Myfristclaa("reem",33)
m.fun()
m.age =40
del m.age
del m
print(m.age)