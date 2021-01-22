import statistics #lib for exercise lvl 2 calcs
# -----------------------------------------------------#
#Exercise 

#1
empty_list = []
#2
q2_list = ["Apple","Orange","Maple","Rice","Tran"] #list with 5 items
#3
print(len(q2_list)) #list length
#4
item1, item2, item3, item4, item5 = q2_list
print(item1,item3,item5) #get list item
#5
mix_data_types = ["Thien", 20, 170, False, "Some Street"] #mix data type 
#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#7
print(it_companies)
#8
print(len(it_companies))
#9
fb, g, m, a, i, o, am = it_companies
print(fb, a, am)
#10
it_companies[0] = "Netflix" #modifying one item
print(it_companies)
#11
it_companies.append("Quick Apps") #add item to list 
print(it_companies)
#12
it_companies.insert(1,"3T") #insert item to index 1
print(it_companies)
#13
it_companies[0] = "NETFLIX" #change item to uppercase 
print(it_companies)
#14
q14_str = "#; "
print(q14_str.join(it_companies)) #join str with list
#15
q15_exist = "NETFLIX" in it_companies #check if item exist 
print(q15_exist)
#16
it_companies.sort()
print(it_companies) #sort item in ascending order
#17
it_companies.sort(reverse=True) #sort item in descending order
print(it_companies)
#18
it_companies.reverse()
print(it_companies) #reverse item
#18 
firstthree_company = it_companies[0:3] #show the first three
print(firstthree_company)
#19
lastthree_company = it_companies[6:9] #show the last three
print(lastthree_company)
#20
print(it_companies[4]) #show the middle 
#21
del it_companies[0] #remove the first 
print(it_companies)
#22
del it_companies[3] 
print(it_companies) #remove the middle 
#23
"""del it_companies[9] #error 
print(it_companies)"""
"""#24
del it_companies
print(it_companies)""" #error
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_list = front_end + back_end #join 2 list 
print(join_list)
#27
full_stack = join_list

#Exercise Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() #sort list 
print(min(ages),max(ages)) #min, max

ages.append(min(ages)) #add min to current list
ages.append(max(ages)) 

print(statistics.median(ages)) #use stats lib for median

print(statistics.mean(ages))

ages_range = max(ages) - min(ages)
print(ages_range) #range of list 

min_val = min(ages) - statistics.mean(ages)
max_val = max(ages) - statistics.mean(ages)
print((abs(max_val)),abs(min_val)) #used abs to compare min_val and max_val

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
#2
print(statistics.median(countries))
#3
countries_one = countries[:len(countries)//2] #divide length of countries based on slice
countries_two = countries[len(countries)//2:] #into 2 equal parts 
print(countries_one)
#4
lst = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
cn, rs, usa, *scandic = lst
print(scandic) #unpack first 3 items in list. used *scandic as rest of items
