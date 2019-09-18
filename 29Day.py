name =["Arwa","Bader","saad","slman"]
for x in name:
    print(x)

print("------------------letters in the word Bader-------------------------")
for y in "Bader":
    print(y)

#Exit the loop when x is "saad"
print("-------------------------------------------")
for z in name:
    print(z)
    if z =="saad":
        break

#Exit the loop when x is "saad", but this time the break comes before the print
print("-------------------------------------------")
for z in name:
    if z == "saad":
        break
    print(z)

#Do not print saad.
print("-------------------------------------------")
for z in name:
    if z == "saad":
        continue
    print(z)
