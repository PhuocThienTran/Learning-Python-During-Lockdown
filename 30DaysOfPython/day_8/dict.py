# -----------------------------------------------------#
#Exercise 

#1
dog = {}
#2
dog = {
    "name" : "Barnaby", 
    "color": "Brown", 
    "breed" : "German Shepherd"
    }
print(dog)
#3
student = {
    "first_name" : "Thien", #string 
    "last_name" : "Tran", #string
    "gender" : "Male", #string
    "age" : 20,
    "marriage" : False, #boolean
    "skills" : ["JavaScript", "JSON", "HTML", "CSS", "PHP", "Python"], #list
    "country" : "Vietnam",
    "city" : "Ho Chi Minh City",
    "address" : { #dictionary
        "street" : "Some Street",
        "Code" : "10000"
        }
    }
#4
print(len(student))
#5
print(len(student.get("skills")))
print(type(student.get("skills"))) #check "skills" data type
#6
student["skills"].append("Adobe Creative Cloud") #add item to "skills"
print(student)
#7
student_keys = student.keys() #obtain dict's keys
print(student_keys)
#8
student_values = student.values() #obtain dict's values
print(student_values)
#9
print(student.items()) #change dict to tuples
#10
student.pop("marriage")
print(student)
#11
del dog 
