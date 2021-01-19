# -----------------------------------------------------#
#Exercise 

#1
empty_tpl = tuple() #empty tuple
#2
q2_brothertpl = ("Thuan", "Thanh", "Bao")
q2_sistertpl = ("Han", "Ngan", "Vy")
#3
siblings = q2_brothertpl + q2_sistertpl
#4
print(len(siblings))
#5
q5_siblings = ("Thu", "Tho")
family_members = siblings + q5_siblings
#6
print(siblings)
print(q5_siblings)
#7
fruits = ("strawberry", "mango", "banana", "apple")
veg = ("carrot", "salad", "kale")
animals = ("dog", "cat", "fish", "bird")
food_stuff_tp = fruits + veg + animals
#8
food_stuff_lt = list(food_stuff_tp) #change tuple to list
#9
middle_food_stuff_lt = food_stuff_lt[5:6]
print(middle_food_stuff_lt)
#10
first_three_lt = food_stuff_lt[0:3]
last_three_lt = food_stuff_lt[-3:] #last three terms
print(first_three_lt,last_three_lt)
#11
del food_stuff_tp #delete entire tuple
#12
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(("Estonia" in nordic_countries),("Iceland" in nordic_countries)) #check items in tuple

# -----------------------------------------------------#

"""
lists [], tuples ()
"""
