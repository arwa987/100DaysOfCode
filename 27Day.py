num =9
num2 = 3

if num> num2 :
    print("The num is greater than num2")



#If statement, without indentation (will raise an error)
"""
if num> num2 :
print("The num is greater than num2")
"""

#elif
a =7
b =7
if a > b :
    print("The num is greater than num2")
elif a == b:
    print("a is equal b")

#-------------------------------------------------------------------------

x =30
y =98

if x > y:
    print("x is greater than y ")
elif x == y:
    print("x is equal y")
else:
    print("y is greater than a")

#--------------------------------------------------------------------------

if x > y:
    print("x is greater than y ")
else:
    print("y is greater than a")

#---------------------------------------------------------------------------
if x < y: print("x is less than y")
#---------------------------------------------------------------------------
print("x") if x < y else print("y")
#---------------------------------------------------------------------------
print("=") if x == y else print("x") if x < y else print("y")
#---------------------------------------------------------------------------
n =900
n2 =90
n3 = 9
if n2 > n3 and n > n2 :
    print("Both condition is true")

#---------------------------------------------------------------------------
if n3 >n2 or n>n2:
    print("At lest one of the condition is true")
#---------------------------------------------------------------------------
z = 500
if z > 100 :
    print("Above 100")
    if z > 200:
        print("and also above 200")
    else :
        print("but not above 200")


