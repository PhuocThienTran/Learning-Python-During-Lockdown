# -----------------------------------------------------#
#Exercise 

#1
q1_string1, q1_string2, q1_string3, q1_string4, q1_space = "Thirty","Days","Of","Python", " "
q1_joinstring = q1_string1 + q1_space + q1_string2 + q1_space + q1_string3 + q1_space + q1_string4
print(q1_joinstring)

#2 - 13
#2
q2_string1, q2_string2, q2_string3, q2_space = "Coding", "For", "All", " "
#3
company = q2_string1 + q2_space + q2_string2 + q2_space + q2_string3
#4
print(company)
#5
print(len(company))
#6
uppercase_str = "coding for all"
print(uppercase_str.swapcase()) #converts str to uppercase
#7
lowercase_str = "CODING FOR ALL"
print(lowercase_str.swapcase())
#8
print(company.capitalize()) #capitalise first letter
print(company.title()) #returns a cased string
print(company.swapcase()) 
#9
slice_str = company[7:13] #cut the Coding word 
print(slice_str)
#10
print("Coding" in company) #check if Coding is in company str
#11
print(company.replace("Coding", "coding")) #replace Coding to coding in company str
#12
str_q12_1 = "Python for Everyone"
str_q12_2 = "Python for All"
print(str_q12_1.replace(str_q12_1,str_q12_2)) #replace str_q12_1 -> str_q12_2
#13
print(company.split()) #splits the string
#14
q14_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(q14_string.split(", ")) #splits the string into different index
#15
print(company[0])
#16
print(company[-1])
#17
print(company[10])
#18
PFE = str_q12_1 # acronym for str in q12
#19
CFA = company 
#20
sub_CFAstr = "C"
print(CFA.index(sub_CFAstr)) #lowest index of str similar to the find method
#21
sub_CFAstrF = "F"
print(CFA.index(sub_CFAstrF))
#22
CFAP = "Coding For All People"
print(CFAP.rfind("l"))
#23
q23_string = "You cannot end a sentence with because because because is a conjunction"
sub_q23string = "because"
print(q23_string.index(sub_q23string))
#24
print(q23_string.rindex("because"))
#25
slice_str_q23_string = q23_string[31:54]
print(slice_str_q23_string)
#26 - 27 are already done
#28
print(CFA.startswith("Coding")) #start with "Coding" in CFA str
#29
print(CFA.endswith("coding"))
#30
"""q30_string = "'   Coding For All      '" 
print(q30_string.strip("'   '"))#strip the gap between str""" #minor bug
#31
challenge = '30DaysOfPython'
print(challenge.isidentifier()) #check for valid in var name
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) 
#32
python_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(python_lib)) #join str together
#33
print("I am enjoying this challenge.\nI just wonder what is next.")
#34
print("Name\tAge\tCountry")
print("Thien\t20\tVietnam")
#35
radius = 10
pi = 3.14
area = int(pi * radius ** 2)
area_of_circle = 'The area of circle with radius {} is {}.'.format(radius, area)
print(area_of_circle)
#36
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')