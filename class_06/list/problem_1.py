## write a program to store seven fruits in list entered by user and print them
fruits = []
for i in range(1,8):
    userInput = input("Enter any fruit name :")
    fruits.append(userInput)
print(fruits)