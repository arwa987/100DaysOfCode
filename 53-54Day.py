import module
print("The result 1+8 is:")
module.funsum(1,8)
print("The result 4-2 is:")
module.funsub(4,2)
print("The result 6*6 is:")
module.funmul(6,6)
print("The result 8/2 is:")
module.fundiv(8,2)



import datetime
x =datetime.datetime.now()
print(x.year)
print(x)
print(x.month)
print(x.day)

import datetime
x =datetime.datetime.now()
ye =x-datetime.timedelta(days=1)
to =x+datetime.timedelta(days=1)
print("yesterday",ye)
print("tomorrow",to)

