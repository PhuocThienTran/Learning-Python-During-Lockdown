#1
q1_count = 0
while q1_count < 10:
    q1_count += 1
    print(q1_count) 
#2
q2_count = 11
while q2_count > 0:
    q2_count -= 1
    print(q2_count)
#3
q3_str = ""
while q3_str < "#######": 
    q3_str += "#"
    print(q3_str)
#4
length = int(input("Please Enter any Length of #  : "))
i = 0
while(i < length):
    j = 0
    while(j < length):      
        j = j + 1
        print('#', end = ' ')
    i = i + 1
    print()
#5
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers: 
    print(number, "x", number, "=", number * number) #take number "x" number "=" number * number

#6
random_stuffs = ['Python', 'Numpy','Pandas','Django', 'Flask']
for stuffs in random_stuffs:
    print(stuffs) 

#7
even_start, even_end = 0, 100
for num in range(even_start, even_end + 1): #increment by 1 
    if num % 2 == 0: #num % 2 == 0
        print(num, end = " ") 

#8
odd_start, odd_end = 0, 100
for odd_num in range(odd_start, odd_end + 1):
    if odd_num % 2 != 0:
        print(odd_num, end = " ") 

#9
n = 100
sum = 0
for counter in range(0,n+1): #start at 0, end at 100
    sum = sum + counter
print("The sum of all numbers is", sum)

#10
maximum = int(input(" Please Enter the Maximum Value : "))
even_total = 0
odd_total = 0
 
for number in range(0, maximum + 1):
    if(number % 2 == 0):
        even_total = even_total + number
    else:
        odd_total = odd_total + number
 
print("The Sum of Even Numbers from 0 to {0} = {1}".format(number, even_total)) #{0} is maximum, {1} is even_total
print("The Sum of Odd Numbers from 0 to {0} = {1}".format(number, odd_total))

#12
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in reversed(fruits):
    print(fruit)