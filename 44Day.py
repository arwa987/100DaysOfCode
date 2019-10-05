class Supper:
    def __init__(self,name,age):
        self.name =name
        self.age =age

    def display(self):
        print(self.name,self.age)

class sub(Supper):
    def __init__(self,name,age,ID,Lname):
        super().__init__(name,age)
        self.ID =ID
        self.lname =Lname

    def welcome(self):
        print("Wlcome",self.name,self.lname,"to my system")


a = sub("sam",23,12356,"alhrbi")
print(a.ID)
print(a.lname)
a.welcome()