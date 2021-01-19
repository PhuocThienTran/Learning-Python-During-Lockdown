ss = ["spam", 2.0,5,[10,20]]
print(ss[3])
print("spam" in ss)

nums = [1,2,3,4,5]
for i in range(len(nums)): # the loop tranverse the list and updates each element
    nums[i] = nums[i] * 2 # by 2
print(nums)

a = [1,2,3] 
b = [4,5,6]
c = a + b # this concatenates the list
print(c)

d = [1,2,3] * 3 #repeats the list 3 times
print(d) 

numlist = [] #make empty list
while True:
    inp = input("Enter a number: ")
    try:
        inp = int(inp)
        numlist.append(inp) #append the number to the list everytime 
    except:
        if inp == "done": #if input = done, break loop
            break
        print(inp, "Is Invalid Number") #if not int, then invalid
average = sum(numlist) / len(numlist) #the sum of list / length of list
print("Average: ", float(average))

str = "Ishini-Tennakoon-Hewage-Tennakoon"
str_delimeter = "-"
print(str.split(str_delimeter))

    