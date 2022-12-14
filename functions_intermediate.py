
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# 1. Update Values
x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

z[0]['y'] = 30
print(z)


# 2. Iterate through a list
def iterateDictionary(some_list):
    for x in some_list:
        print(f"first_name - {x['first_name']}, last_name - {x['last_name']}")

iterateDictionary(students)


# 3. Get values from a list
def iterateDictionary2(key_name, some_list):
    for x in some_list:
        print(x[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# 4. Iterate through a dictionary with list values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(len(some_dict['locations']), "LOCATIONS")
    for x in range (len(some_dict['locations'])):
        print(some_dict['locations'][x])

    print(len(some_dict['instructors']), "INSTRUCTORS")
    for x in range (len(some_dict['instructors'])):
        print(some_dict['instructors'][x])

printInfo(dojo)

