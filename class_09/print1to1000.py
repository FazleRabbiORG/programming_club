# print from 1 to 1000 using while loop 

i = 1
while i <= 1000:
    print(i, end= "\t" if i % 10 != 0 else "\n")
    i += 1
