# Days 2: 30 Days of Python Programming
# -----------------------------------------------------#

#Exercise 1
firstname = "Thien"
lastname = "Tran"
fullname = "Tran Phuoc Thien"
country = "Vietnam"
city = "Ho Chi Minh"
age = "20"
year = "2020"
is_married = False
is_true = False 
is_light_on = False
first_name, middle_name, last_name = "Thien", "Phuoc", "Tran"

#Exercise 2 
print(type(firstname)) 
print(type(is_married))
print(len(lastname))
print(len(firstname))

num_one, num_two = 5,4
_total = (num_one + num_two)
print(_total)

_diff = (num_one - num_two)
print(_diff)

_product = (num_one * num_two)
print(_product)

_division = (num_two / num_one)
print(_division) 

_remainder = (num_two % num_one)
print("Remainder", _remainder)

_exp = (num_one**num_two)
print(_exp)

_floor_division = (num_two//num_one)
print(_floor_division)

radius = float(30) 
pi = 3.14

area_of_circle = (pi * radius**2)
print(area_of_circle)

circum_of_circle = (2*radius*pi)
print(circum_of_circle)


first_name = input("Thien")
last_name = input("Tran")
_country = input("Vietnam")
_age = input("20")

print(first_name,last_name,_country,_age)
