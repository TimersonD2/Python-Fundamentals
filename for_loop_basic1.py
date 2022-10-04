# print all integers from 0 to 150
for x in range(150):
    print(x)

# print all the multiples of 5 from 5 to 1,000
for x in range(5,1000, 5):
    print(x)

# counting, the dojo way
for x in range(1, 100):
    if (x % 10 == 0):
        print ('Coding Dojo')
    elif (x % 5 == 0):
        print('Coding')
    else:
        print(x)

# whoa. that suckers huge
sum = 0
for x in range(500000):
    if (x % 2 == 1):
        sum = sum + x

print('the sum of odd numbers is:', sum)

# countdown by fours
for x in range(2018, -4, -4):
    if (x >= 0):
        print(x)


# flexible counter
lownum = 1
highnum = 20
mult = 3

while lownum <= highnum:
    if (lownum % mult == 0):
        print(lownum)
    lownum = lownum + 1


