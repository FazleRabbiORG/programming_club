#get user name and check is it's length is less then 10 character

username = input("Enter your name: ")
if len(username) < 10:
    print("Your name is less then 10 character")
else:
    print("Your name is more then 10 character")