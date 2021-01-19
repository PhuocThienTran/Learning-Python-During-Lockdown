# -----------------------------------------------------#
#Exercise 

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1
print(len(it_companies), "IT Companies")
#2
it_companies.add("Twitter") #add item to set
print(it_companies)
#3
it_companies.update(["Quick Apps", "3T", "BIDV"]) #add multiple items to set
print(it_companies)
#4
it_companies.remove("Facebook") #remove item from set
print(it_companies)
#5
print("The difference between remove and discard is if item doesn't exists in set \nremove will appear with error, but discard wouldn't raise error.")
#6
q6_st = A.union(B) 
print(q6_st)
#7
q7_st = A.intersection(B)
print(q7_st)
#8
print(A.issubset(B))
#9
print(A.isdisjoint(B))
#10
A.update(B)
print(A)
B.update(A)
print(B)
#11
print(A.symmetric_difference(B))
#12
del it_companies
del A
del B
#13
q13_st = set(age)
print("The length of age's set is < length of age's list: ", len(q13_st) < len(age)) #compare length of given set and list
#14
print("""List are mutable - can be converted into another data type and defined under [].\n
Tuple aren't immutable and defined under ().\n
Set are unordered collection of elements, are mutable - but only immutable objects can be stored, and defined under {}""")
#15
#cant do this one ;-;
# -----------------------------------------------------#
"""
    list [], tuple (), set {}
"""