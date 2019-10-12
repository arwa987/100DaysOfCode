import datetime
x =datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime('%A'))

import datetime
x =datetime.datetime(2098,7,3)
print(x)

import datetime
x = datetime.datetime(2019,10,8)
print(x.strftime("%B"))
print(x.strftime("%b"))