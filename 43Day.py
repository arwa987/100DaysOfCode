class Supper:
    def __init__(self,name,age):
        self.name =name
        self.age =age

    def display(self):
        print(self.name,self.age)

class sub(Supper):
    def __init__(self,name,age):
        Supper.__init__(self,name,age)


a = sub("sam",23)
a.display()
