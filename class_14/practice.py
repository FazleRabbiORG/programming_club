#taking input from user name and date

name = input("Enter your name: ")
print( name)
date = input("Enter your date of birth: ")
print("Date ", date)


letter = """Dear name
            Your are selected
            date"""

#replace name and date with user name and date
# letter.replace("name", name)
# letter.replace("date", date)

print(letter)

letter =  letter.replace("name", name).replace("date", date)
print(letter)
