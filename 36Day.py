def myfu (x):
    return lambda a :a*x

b =myfu(2)
b2 =myfu(3)

print(b(11))
print(b2(11))