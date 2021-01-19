word = "Ishini"
def backward(word):
    index = len(word) - 1
    while index >= 0:
        print(word[index])
        index -= 1
backward(word)


fruit = "apple"
def count(fruit, count):
    count = 0
    for letter in fruit:
        if letter == "p":
            count = count + 1
    print("Amount of p:", count)
count(fruit,"p")


q4_word = "tennakoon"
print("Amount of n: ", q4_word.count("n"), "Amount of o: ", q4_word.count("o"))


str = "X-DSPAM-Confidence:0.8475"
colon = str.find(":")
print("Find the index of (:)", colon)
last_num = str.find("5")
print("Find the index of 5: ", last_num)
slice_str = str[colon+1:last_num] #start from colon + 1 to get number 0
print("Convert str to float", float(slice_str))

