import math

mbox_shortfile = open("chapter7/txtfiles/mbox-short.txt")
for line in mbox_shortfile:
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != "From":
        continue
    print(words[2])



mbox_shortfile = open("chapter7/txtfiles/mbox-short.txt")
for line in mbox_shortfile:
    words = line.split()
    if len(words) == 0 or words[0] != "From":
        continue
    print(words[2])


romeo_list = [] #create empty list of words
romeofile = open("chapter8/txtfiles/romeo.txt")
for line in romeofile: 
    words = line.split() #split the line into the list of words
    for word in words: #check if a word is already in the list
        if word in romeo_list:
            continue
        romeo_list.append(word) #if the word isn't in the list, add it to it
print(sorted(romeo_list)) #sort the list alphabetical


mbox_shortfile = open("chapter7/txtfiles/mbox.txt")
count = 0 #line count = 0 at first
for line in mbox_shortfile:
    line = line.rstrip() 
    if line.startswith("From: "): #line starts with From
        words = line.split() #split the lines into words
        print(words[1]) #only print the second word from "From"
        count += 1 #continue the line count 
print("There were", count, "lines in the file with From as the first word")



numlist = [] #make empty list
while True:
    inp = input("Enter a number: ")
    try:
        inp = int(inp)
        numlist.append(inp) #append the number to the list everytime 
    except:
        print(inp, "Is Invalid Number") #if not int, then invalid
        if inp == "done": #if input = done, break loop
            break
print("Maximum: ", float(max(numlist)))
print("Minimum: ", float(min(numlist)))







