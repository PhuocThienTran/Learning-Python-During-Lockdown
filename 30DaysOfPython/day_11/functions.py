#1
def add_two_numbers():
    num1 = 5
    num2 = 3
    total = num1 + num2
    return total
print(add_two_numbers())

#2
def area_of_circle(r):
    Pi = 3.14
    area = Pi * r ** 2
    return area
print(area_of_circle(10))

#3
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(add_all_nums(2,3,5))

if(type(add_all_nums()) == int):
    print("Yes")
else:
    print("No")

#4
def convert_celcius_to_fahrenheit(F, C): #this is incorrect
    F = (C * 9/5) + 32
    return C
print(convert_celcius_to_fahrenheit(50,32))

#5
def check_season (month): 
    months = [[12 , 1 , 2],[3 , 4 , 5],[6 , 7 , 8],[9 , 10 , 11]] 
    if month in months[0]: 
        print("WINTER") 
    elif month in months[1]: 
        print ("SPRING") 
    elif month in months[2]: 
        print ("SUMMER") 
    elif month in months[3]: 
        print ("AUTUMN") 
month = 5
print("For Month number:", month)
check_season ( month) 

#6
def calculate_slope(x1,x2,y1,y2):
    slope = (y2 - y1)/(x2 - x1)
    return slope
print(calculate_slope(10,5,10,20))

#7
def solve_quadratic_eqn(a,b,c):
    x = (b**2) - (4*a*c)
    return x 
print(solve_quadratic_eqn(8,9,10))

#8
def print_list (names,*list_names):
    print(names)
    for i in list_names:
        print(i)
print_list('Team: ','Barnaby','Thien','Ishini')

#9
def reverse_list(r_list_names):
    for j in reversed(r_list_names):
        print(j)
reverse_list(["A", "B", "C"])

#10

#11
def add_item():
    global num_list
    num_list = [1,2,3,4,5]
    num_list.extend((6,7,8))
    return num_list
add_item()
print(num_list)

#12
def remove_item():
    global lang_list
    lang_list = ["html","python","css"]
    lang_list.remove("python")
    return lang_list
remove_item()
print(lang_list)

#13