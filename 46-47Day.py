class Library :
    def __init__(self,book,shelf):
        self.book =book
        self.shelf =shelf



object =Library(300,45)
print("the number of book is ",object.book,"and shelf is",object.shelf)

class science_section(Library):
    def __init__(self,book,shelf,name):
        super().__init__(book,self)
        self.name =name

    def display(self):
        print("we have ",object.book,"and shelf",object.shelf,
              "and we have section",self.name)



x =science_section(20, 4,"physic books")
x.display()



