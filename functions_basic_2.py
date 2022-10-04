# CountDown function
def count_down(num):
    numList = []
    for num in range(num, -1, -1):
        numList.append(num)

    print(numList)
    return(numList)

returnList = count_down(10)
print(returnList)

# Print and Return function
def print_return(a,b):
    print(a)
    return(b)

num = print_return(5,9)
print(num)


# Adds first value to the list length returns the sum
def value_plus_length(numList):
    length = len(numList)
    sum = numList[0] + length
    print(sum)
    return(sum)

numList = [12,6,9,12]
returnSum = value_plus_length(numList)
print(returnSum)


# Values greater than the second
def values_gt_second(numList):
    gtList = []
    length = len(numList)
    secondNum = numList[1]
    if(length < 2):
        return(False)
    for x in range (length):
        if (numList[x] > secondNum):
            gtList.append(numList[x])
    
    return(gtList)

numList = [1,4,3,4,5,6,7,8,9]
returnValue = values_gt_second(numList)
print(returnValue)



# This Length, That value
def length_value(length,value):
    numList = []
    for x in range(length):
        numList.append(value)

    return(numList)

returnList = length_value(2,9)
print(returnList)




