# -----------------------------------------------------#
#Exercise 

#1-3
age = 20
height = float(1.70) 
complex_num = 1 + 1j

#4
base = 20
height_tri = 10
area_of_tri = 0.5 * 20 * 10
print(int(area_of_tri))

#5
side_a, side_b, side_c = 5,4,3
peri_of_tri = 5 + 4 + 3
print(int(peri_of_tri))

#6
area_of_rect = 20 * 10
print(int(area_of_rect))

peri_of_rect = 2 * (20 + 10)
print(int(peri_of_rect))

#8
slope = 1 # y = 2x - 2 -> 2 = 2x -> x = 1

#9
y2, y1, x2, x1 = 10, 2, 6, 2
slope_point = y2-y1/x2-x1
print(int(slope_point))

#10
print(slope_point > slope)

#11
y = 0
y = (-3 ** 2 + (6*-3) + 9)
print(y == 0)

#12
print(len("python") != len("jargon"))

#13
print("on" in "jargon" and "on" in "python")

#14
print("jargon" in "I hope this course isn't full of jargon")

#15
print("on" not in "dragon" and "python")

#16
float(len("python"))
print(str(float(len("python"))))

#17
num = int(input("Enter a number: "))
if(num % 2 ) == 0:
    print("{0} is even number".format(num))
else:
    print("{0} is odd number".format(num))

#18
floor_div = 7 // 3
print(float(floor_div))

#19
print(type("10") == 10)

#20
print(type("9.8") == 10)

#21
hours = 40
rate_per_hour = 28
weekly_earning = hours * rate_per_hour
print(weekly_earning)

#22
year = int(input("Enter number of years you have lived: "))
number_of_second = 31556926 * year
print("You have lived for {0}".format(number_of_second),"seconds")

#23
print("""1 1 1 1 1
2 1""",2*1,2*2,2*4,"""
3 1""",3*1,3*3,3*9,"""
4 1""",4*1,4*4,4*16,"""
5 1""",5*1,5*5,5*25)
