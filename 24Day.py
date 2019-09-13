x =  {
    "name":"ali",
    "age":20,
    "years":2000
}
#Make a copy of a dictionary with the copy () method
x2 =x.copy()
print(x2)

#Make a copy of a dictionary with the dict() method
x3 = dict(x)
print(x3)

#Create a dictionary that contain three dictionaries
myfamily ={
    "Boy1":{
        "name" :"ali",
        "years": 2009
    },
    "Boy2":{
        "name":"ahmad",
        "years":2000
    },
    "Boy":{
        "name":"slman",
        "years":2005
    }
}
print(myfamily)

#The dict() Constructor
me =dict(ID =123, name ="AR", years =2008)
print(me)