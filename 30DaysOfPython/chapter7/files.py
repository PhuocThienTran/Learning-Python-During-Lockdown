open_file = open("chapter7/txtfiles/mbox.txt")

file_name = input("Enter the file name: ") #check if file exists
try:
    open_file = open(file_name)
except:
    print("File doesn't exist: ", file_name)
    exit()

line_count = 0 
for line in open_file:
    line_count += 1 #count number of lines in the opened file
    
    line = line.rstrip() 
    if not line.startswith("From: "): #check if line in file starts with "From", if not continue (pass that line)
        continue
    print(line)
print("Line Count in Opened File: ", line_count)
