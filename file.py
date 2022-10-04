num1 = 42   # variable declaration - primitive - number
num2 = 2.3  # variable declaration - primitive - number
boolean = True  # variable declaration - primitive - boolean
string = 'Hello World'  # variable declaration - primitive - string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')   # intialize a Tuple
print(type(fruit))  
print(pizza_toppings[1])    # log the second item  in the pizza toppings list
pizza_toppings.append('Mushrooms')  # add value to the list
print(person['name'])   # log the value of 'name' from the dictionary called person
person['name'] = 'George'   # assign a value to 'name' from the dictionary called person
person['eye_color'] = 'blue'    # assign a value to 'eye_color' from the dictionary called person
print(fruit[2]) # log the third item from the Tuple called fruit

if num1 > 45:   # IF statement start
    print("It's greater")   # if num1 greater than 45 log it's greater
else:
    print("It's lower") # else log it's lower, end of IF statement

if len(string) < 5: # IF statement start
    print("It's a short word!") # if the length of the variable called string is less than 5, log short world
elif len(string) > 15:
    print("It's a long word!")  # else if length of string greater than 15, log long world
else:
    print("Just right!")    # else log just right, neither the if nor the else if were true

for x in range(5):  # for loop start, using variable x it executes 5 times
    print(x)    # log the value of the variable x, end of for loop
for x in range(2,5):    # for loop start, x starts at 2 ends at 5
    print(x)    # log the value of x
for x in range(2,10,3): # for loop start, x starts at 2, increments by 3, ends with 8
    print(x)    # log the value of x
x = 0   # initialize the variable x with the value of 0
while(x < 5):   # while loop start, excutes while x is less than 5
    print(x)    # log the value of x
    x += 1      # increment the value of x

pizza_toppings.pop()    # delete the last value of the list called pizza_toppings
pizza_toppings.pop(1)   # delete the second value of the list

print(person)   # log the dictionary called person
person.pop('eye_color')     # delete the dictionary item called eye_color
print(person)   # log the dictionary called person after the pop

for topping in pizza_toppings:      # for loop start executes for each value of list called pizza_toppings
    if topping == 'Pepperoni':  # IF variable topping equals pepperoni loop returns to the top
        continue                # returns to top of loop
    print('After 1st if statement')     # executes if variable topping does not equal pepperoni
    if topping == 'Olives':     # compares the value of topping to olives
        break                   # if topping equals olives for loop ends

def print_hello_ten_times():    # defines and starts a function called print_hello_ten_times
    for num in range(10):       # for loop start, variable num has range of 10
        print('Hello')          # prints the string hello, end of for loop

print_hello_ten_times()         # executes the function named print_hello_ten_times

def print_hello_x_times(x):     # defines and starts a function called print_hello_x_times, recieves one parameter x
    for num in range(x):        # for loop start, vaiable num with range equal to value of variable x
        print('Hello')          # prints the string hello, end of for loop

print_hello_x_times(4)          # executes the function named print_hello_x_times, passes in the number 4

def print_hello_x_or_ten_times(x = 10): # defines and starts a function, parameter x defaults to 10
    for num in range(x):                # for loop start, variable num with range of function parameter x
        print('Hello')                  # print string hello, end of for loop, end of function

print_hello_x_or_ten_times()    # executes function named print_hello_x_or_ten_times without parameter, default is 10
print_hello_x_or_ten_times(4)   # executes funtion print_hello_x_or_ten_times with parameter value of 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)