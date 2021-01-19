open_file = open("chapter7/txtfiles/mbox-short.txt")
for line in open_file:
    line_upper = line.rstrip().upper()
    print(line_upper)


file_name = input("Enter a file name: ")
try:
    open_file = open(file_name)
except:
    print("File doesn't exist: ", file_name)
    exit()
count = 0
confidencesum = 0
for line in open_file:
    if line.startswith('X-DSPAM-Confidence: '): 
        count += 1 #count every time X-DSPAM line is spotted
        confidence = float(line[20:-1]) #20 is where the number starts, -1 is the last number
        confidencesum += confidence
averageconfidence =  confidencesum/count
print ("Average spam confidence: ", str(averageconfidence))


filename = input("Enter a file name: ")
try:
    openfile = open(filename)
except:
    if filename == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!", filename)
    else:
        print("File doesn't exist: ", filename)
        exit()
subject_line_count = 0
for subject_line in openfile:
    if subject_line.startswith("Subject:"):
        subject_line_count += 1
print("There were", subject_line_count, "subject lines in", filename)


