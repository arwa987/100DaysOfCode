x =99
def numfun():
    x =67
    print(x)


numfun()
print(x)

#Global Keyword
def numfuc2():
    global y
    y =300

numfuc2()
print(y)



z =900
def numf():
    global z
    z=890

numf()
print(z)