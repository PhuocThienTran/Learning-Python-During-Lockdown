import math
import random

print("Number of Letters: ", len("Ishini Tennakoon Hewage Tennakoon"))

for i in range(10): #run the for loop 10 times
    x = random.randint(0,100)
    print(x)

def print_proglang():
    print("HTML, CSS, PHP")
    print("JavaScript, Python")
print(print_proglang)

def repeat_proglang():
    print_proglang()
    print_proglang()
repeat_proglang()

def print_name(fname,lname):
    print(fname + lname)
print_name(("Thien","Tran"),("Ishini","Tennakoon"))

def add_two(a,b):
    added = a + b
    return added
x = add_two(3,5)
print(x)

#questions
def computepay(hours,rate,overtime):
    pay = (hours * rate) + overtime
    return(pay)
pay = float(computepay(int(input("Enter Hours: ")), int(input("Enter Rate: ")), 25))
print("Pay: ", pay)


def computegrade(score):
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
    return(score)
try:
    score = float(computegrade(float(input("Enter Score: "))))
except:
    print("Bad score")

    