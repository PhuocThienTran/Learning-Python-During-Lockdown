# -----------------------------------------------------#
#Exercise 

#1
user_input = int(input("Enter your age: "))
if user_input >= 18:
    print("{0} means you are old enough to learn to drive".format(user_input))
elif user_input < 18:
    user_input = int(18) - user_input #take user input = 18 as integer - user input to figure out years
    print("You need {0} more years to learn to drive".format(user_input))

#2
age = int(input("Enter your age: "))
your_age = 30 #max amount of years
if age <= 30:
    age = int(30) - age #take age = 30 as integer - age to figure out amount of years younger
    print("You are {0} years younger".format(age))
elif age >= 30:
    age = age - int(30)
    print("You are {0} years older".format(age))

#3
first_num = int(input("Enter First Number: "))
second_num = int(input("Enter Second Number: "))
if first_num > second_num:
    print("{0} is greater than {1}".format(first_num, second_num)) #{0} is first_num, {1} is second_num hence format
elif first_num < second_num:
    print("{0} is less than {1}".format(first_num, second_num))
elif first_num == second_num:
    print("{0} is equal to {1}".format(first_num, second_num))


#4
student_score = int(input("Enter your score: "))
if 0 <= student_score <= 49:
    print("F")
elif 50 <= student_score <= 59:
    print("D")
elif 60 <= student_score <= 69:
    print("C")
elif 70 <= student_score <= 89:
    print("B")
elif 90 <= student_score <= 100:
    print("A")

#5
month = input("Enter Month: ")
if month in ("September", "October", "November"):
    print("Season is Autumn")
elif month in ("December", "January", "February"):
    print("Season is Winter")
elif month in ("March", "April", "May"):
    print("Season is Spring")
elif month in ("June", "July", "August"):
    print("Season is Summer")

#6
fruits_input = input("Input a Fruit: ")
fruits = ['banana', 'orange', 'mango', 'lemon']
if fruits_input not in fruits: #if fruits_input isn't in fruits, then append the fruits_input into fruits then print the new fruits
    fruits.append(fruits_input)
    print(fruits)
elif fruits_input in fruits:
    print("That fruit already exist in the list")

#7
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if "skills" in person.keys():
    print(person.get("skills"[2]))

#this is too hard