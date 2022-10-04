#1 - Will print the number 5
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 - Will print the number ten the result of 5+5
def number_of_military_branches():
    return 5
print(number_of_food_groups() + number_of_military_branches())


#3 - Will print the number 5
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 - Will print the number 5
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 - Will print the number 5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# the second time it prints, it prints None because the function has no return statement
#  and the default value of the variable x is None


#6 - Will print three times - 1st prints the number 3 - 2nd prints the number 5 - 3rd prints the number 8
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# errors the 3rd time it prints because the function has no return statment


#7 - will print 25 as a string
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 - prints the number 100 then prints the number 10
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 - prints the number 7, prints the number 14, finally prints the number 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 - prints the number 8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 - prints the number 500, prints the number 500 a second time, 
#       prints the number 300, prints the number 500
#   There are two separate variables called b. One outside the function, one inside the function.

b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 - prints the number 500, prints the number 300, prints the number 500,
#       prints the number 300, prints the number 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 - prints the number 500,  prints the number 500 a second time, 
#       prints the number 300, prints the number 300 a second time.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 - prints the number 1, prints the number 3, prints the number 2.
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 - prints the number 1, prints the number 3, prints the number 5, 
#       prints the number 10.
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)