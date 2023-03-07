# get userinput and check bangladeshi education grade system and print

number = int(input("Enter your number: "))

if number >= 80 and number <= 100:
    print("A+")
elif number >= 70 and number <= 79:
    print("A")
elif number >= 60 and number <= 69:
    print("A-")
elif number >= 50 and number <= 59:
    print("B")
elif number >= 40 and number <= 49:
    print("C")
elif number >= 33 and number <= 39:
    print("D")
elif number >= 0 and number <= 32:
    print("F")
else:
    print("Invalid number")
