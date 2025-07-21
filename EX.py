def isEqual(list1, list2) :
    return list1 != list2  
# Complete this code !


# MAIN CODE 
list1 = eval(input('list1'))
list2 = eval(input('list2'))

# Write your code here !
if not isEqual(list1, list2):
    print("EQUAL")
else:
    print("NOT EQUAL")


word = input("Your word: ")
modified_word = word.replace('A', '*')
print(modified_word)

# Q3
def removeFirstItem(numbers):
    # Removes the first item from the list and returns the new list
    return numbers[1:]

# MAIN CODE 
values = eval(input())

# Use the function to get the new list
new_arr = removeFirstItem(values)
print(new_arr)

# 4
# MAIN CODE 
listOfNames = eval(input())
newName = input()

# Write your code here !
new_arr = []
new_arr.append(newName)
print(new_arr)

# MAIN CODE 
values = eval(input())

# Write your code here !
has_pair = False
for num in values:
    if values.count(num) >= 2:
        has_pair = True
        break

if has_pair:
    print('HAS PAIR')
else:
    print('HAS NO PAIR')

def sum2By2(numbers):
    result = []
    for i in range(len(numbers) - 1):
        pair_sum = numbers[i] + numbers[i + 1]
        result.append(pair_sum)
    return result

# MAIN CODE
values = eval(input())
print(sum2By2(values))

def removeSevens(numbers):
    result = []
    for num in numbers:
        if num != 7:
            result.append(num)
    return result

# MAIN CODE
values = eval(input())
print(removeSevens(values))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
average = (num1 + num2) / 2
print(average)

# MAIN CODE
array2D = eval(input())

for row in array2D:
    for i in range(len(row)):
        if row[i] == 7:
            row[i] = 8

print(array2D)

# MAIN CODE
array = eval(input())

if not array or not array[0]:
    print([])
else:
    col_sums = []
    for col in range(len(array[0])):
        total = 0
        for row in array:
            total += row[col]
        col_sums.append(total)
    print(col_sums)

array = eval(input())
count = 0
for word in array:
    count += word.count('a') + word.count('A')
print(count) 
# 
# 
def countEven(array):
    count = 0
    for num in array:
        if num % 2 == 0:
            count += 1
    return count

def countOdd(array):
    count = 0
    for num in array:
        if num % 2 != 0:
            count += 1
    return count

# MAIN CODE
array = eval(input())
print(countEven(array))
print(countOdd(array)) 