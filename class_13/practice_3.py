#check prime number from input

num = int(input("Enter number : "))

#check number is prime number 
for i in range(1,num):
    if num % i == 0:
        print("number is prime")
        break

#cph extention for multiple input value