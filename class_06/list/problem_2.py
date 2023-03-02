##write program to accept mark of 6 students and print them in sorted manner
marks = []
for i in range(1,7):
    userInput = int(input("Enter marks of student :"))
    marks.append(userInput)
marks.sort()
print(marks)
