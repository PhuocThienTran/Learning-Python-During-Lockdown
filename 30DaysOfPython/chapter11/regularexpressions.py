import re #regular expression lib

count = 0
user_inp = str(input("Enter a regular expression: "))
file_name = "chapter7/txtfiles/mbox.txt"
open_file = open(file_name)
for line in open_file:
    line = line.rstrip()
    if re.search(user_inp, line):
        count += 1
print(file_name, "had", (count), "lines that matched", user_inp)


revision = [] #initialise list for str to float conversion
file_open = input("Enter file: ")
try:
    openmbox = open(file_open)
except:
    print("Invalid File")
    exit()
for line in openmbox:
    line = line.rstrip()
    revision_num = re.findall("^New Revision: ([0-9.]+)", line) #(): indicate only want findall() to 
    #give back the floating-point number potion of the "New Revision string"
    for val in revision_num: #val: value in the string
        val = float(val) #convert original str val into float val
        revision = revision + [val] #place val into declared list
revision_sum = sum(revision)
count = float(len(revision))
revision_average = revision_sum / count
print(round(revision_average))
