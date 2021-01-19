word = 'brontosaurus'
d = dict()
for character in word:
    if character not in d: #if only 1 character in word, value = 1
        d[character] = 1
    else: #if multiple characters in word, value = that character + 1
        d[character] = d[character] + 1
print(d)


#Exercise
days_dict = dict() #initialise dict
mbox_file = input("Enter a file name: ")
try:
    open_mbox = open(mbox_file)
except:
    print("Invalid File")
    exit()

for line in open_mbox:
    word = line.split() 
    if len(word) < 3 or word[0] != "From": #if the word array < 3 or word[0] doesn't = "From"
        continue #move on to the next iteration 
    if word[2] not in days_dict:
        days_dict[word[2]] = 1 #if word[2] array has 1 value, then value = 1
    else:
        days_dict[word[2]] += 1 #iterate 1 depending on the value of word array
print(days_dict)



message_dict = dict()
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
print(message_dict)

key_max = max(message_dict, key=message_dict.get) #get the maximum key (key) in the message_dict (iterable)
print(key_max,message_dict[key_max]) #maximum message_dict, and its value




domain_dict = dict()
mboxf = input("Enter a file name: ")
try: 
    openfile = open(mboxf)
except:
    print("Invalid File")
    exit()

for domain_line in openfile:
    domain_word = domain_line.split()
    if len(domain_word) < 3 or domain_word[0] != "From":
        continue
    else:
        atpos = domain_word[1].find("@") #search for "@" in domain_word
        domain = domain_word[1][atpos+1:] #domain starts after the atpos
        if domain not in domain_dict:
            domain_dict[domain] = 1
        else:
            domain_dict[domain] +=1
print(domain_dict)






