import math

n = 5
while n > 0:
    print(n)
    n =- 1
print("Launched!")

while True:
    line = input('> ')
    if line == 'done':
        break #this means if input is "done" -> break the while loop
    print(line)
print('Done!')


while True:
    usr_line = input('> ')
    if usr_line[0] == '#':
        continue #finish the current # iteration input, then jump to the next iteration which is the next input without the #
    if usr_line == 'done':
        break
    print(usr_line)
print('Done!')

friends = ['John', 'Barnaby', 'Thien']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')


#questions
total = 0
count = 0
average = 0
while True:
    number = input("Enter a number: ")
    try:
        if number == "done":
            break
        total += float(number)
        count += 1
        average = total / count
    except:
        print("bad data")
print ("Total: ", total, "Count: ", count, "Average: ", average)


numbers = []
while True:
    num = input("Enter a number: ")
    try:
        if num == "done":
            break
        else:
            numbers.append(int(num))
    except:
        print("bad data")

print("Max: ", max(numbers))
print("Min: ", min(numbers))

#Important:
"""
We call the while statement
an indefinite loop because it simply loops until some condition becomes False,
whereas the for loop is looping through a known set of items so it runs through
as many iterations as there are items in the set.
"""

