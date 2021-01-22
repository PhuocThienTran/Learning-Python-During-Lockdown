"""
So Far: 
string = "banana"
lists = ["Hello", 17, 123, ["Josh", 2, 3]] <- Are mutable because can change
the order of items or reassign an item 
dictionary = {"Ishini": "Girlfriend", "Barnaby": "Bestfriend", "Thien": "Myself"} <- Are mutable
tuples = ("a", "b", "c", 2000) <- Are immutable 
"""

message_dict = dict()
message_list = list() # initialise tuple as list to use .append method
mboxfile = input("Enter a file name: ")
try: 
    openmbox = open(mboxfile)
except:
    print("Invalid File")
    exit()

for message_line in openmbox:
    message_word = message_line.split()
    if len(message_word) < 3 or message_word[0] != "From":
        continue
    if message_word[1] not in message_dict:
        message_dict[message_word[1]] = 1
    else:
        message_dict[message_word[1]] += 1

for key, val in list(message_dict.items()): #get a list of the dictionary's key, value pair
    message_list.append((key, val)) #append the key, value pair into the list

    message_list.sort(reverse=True) #sort the list in reverse order

for key, val in message_list[:2]: #print the 2 most people that has the most commits
    print(key, val)


"""
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
message_word[0] = From, [1] = email, [2] = Sat, [3] = Jan, [4] = 5, [5] = time, [6] = year
"""


hour_dict = dict()
hour_list = list()
mboxfile = input("Enter a file name: ")
try: 
    openmbox = open(mboxfile)
except:
    print("Invalid File")
    exit()

for message_line in openmbox:
    message_word = message_line.split()
    if len(message_word) < 3 or message_word[0] != "From":
        continue
    #print(message_word[5])
    
    colon_position = message_word[5].find(":") #look for the first (:) in the time 
    hour_position = message_word[5][:colon_position] #print the first indication of the (:) as hour position
    #print(hour_position)

    if hour_position not in hour_dict:
        hour_dict[hour_position] = 1
    else:
        hour_dict[hour_position] += 1

for key, val in list(hour_dict.items()):
    hour_list.append((key,val))

    hour_list.sort() #sort the list in hour order 

for key, val in hour_list:
    print(key,val) 

