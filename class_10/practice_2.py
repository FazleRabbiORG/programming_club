ls = [33,45,1,3,100,3,6,7,12,22,120]

max = ls[0]
for i in ls:
    if i > max:
        max = i

print("Maximum number is: ", max)

min = ls[0]
for i in ls:
    if i < min:
        min = i

print("minimum number is :",min)