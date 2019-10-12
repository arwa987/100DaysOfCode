import mymodule as mx
B =mx.person['ID']
print(B)


import platform
x =platform.system()
print(x)

import platform
x =platform.system()
print(platform.python_version())

import platform
x =dir(platform)
print(x)


from mymodule import person
print(person['name'])