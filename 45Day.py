list =("Arwa","Bander","Sam","Reem")
it =iter(list)
print(next(it))
print(next(it))
print(next(it))

list2 ="ARWA"
it2 =iter(list2)
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

for x in list:
    print(x)

for x in list2:
    print(x)

class Me:
    def __iter__(self):
        self.x =1
        return self
    def __next__(self):
            y = self.x
            self.x += 1
            return y



obj =Me()
myit =iter(obj)

print("-----------------------------------------------")
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

