##like as json
## dictionary introduction class
## demo of dictionary with 5 students

students = {
    "student1" : {
        "name" : "Fazle Rabbi",
        "age" : 20,
        "marks" : 80
    },
    "student2" : {
        "name" : "Barun kundu",
        "age" : 21,
        "marks" : 90
    },
    "student3" : {
        "name" : "Sohel",
        "age" : 22,
        "marks" : 70
    },
    "student4" : {
        "name" : "Rahul",
        "age" : 23,
        "marks" : 60
    },
    "student5" : {
        "name" : "Rajib",
        "age" : 24,
        "marks" : 50
    }
}

#print all students name
for student in students:
    print(students[student]["name"])

#print all students name and marks
for student in students:
    print(students[student]["name"], students[student]["marks"])


##methods of dictionary
##get() , keys() , values() , items() , pop() , popitem() , clear() , copy() , update()

## clear() method
students.clear()
print(students)

## change first student name
students["student1"]["name"] = "Fazle Rabbi"