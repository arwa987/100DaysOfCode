list=[-4,-6,-5,-1,2,3,7,9,88]
list2 =[]
m =lambda n:n>0

for x in list:
    if(m(x)):
        list2.append(x)

print(list2)


#------------------------------------------------


def fun(num,p):
    if (p<1):
        return 1
    else:
        return num*fun(num,p-1)

print(fun(5,3))




