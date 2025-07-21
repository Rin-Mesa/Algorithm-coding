# 1
arr = eval(input())


object = {}
for i in range(len(arr)):
    object[arr[i]] = i
print(object)

# 2
arr = eval(input())

result = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == arr[i][j]:
            result[arr[i][j]] = len(arr[i][j])
print(result)

# 3
def covertToResult(arr):
    result = ""
    for cher in arr:
        result += cher.lower()
    return result
    
arr2D = eval(input())
new_arr = []
for arr in arr2D:
    new_arr.append(covertToResult(arr))
print(new_arr)

# 4
arr = eval(input())

count_fruit = 0
count_meat = 0
for key in arr:
    if 'fruit' in key:
        count_fruit += 1
    elif 'meat' in key:
        count_meat +=1
print("Fruit:"+str(count_fruit))
print("Meat:"+str(count_meat))

# 5
arr2D = eval(input())
col = int(input())

if col < 0 or col >= len(arr2D):
    print("Out of range")
else:
    for row in arr2D:
        row[col] = '*'
    print(arr2D)

# 6
arr2D = eval(input())
for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        if arr2D[i][j] == 6:
            arr2D[i][j] = 10
print(arr2D)

# 7
arr2D = eval(input())
result = []
for i in range(len(arr2D)):
    total = 0
    for j in range(len(arr2D[i])):
        total += arr2D[i][j]
        average = len(arr2D[i])
    result.append(int(total/average))
print(result)

# 8
arr2D = eval(input())

new = []
for row in arr2D:
    count = 0
    for num in row:
        if num % 2 != 0:
            count += 1
    new.append(count)
print(new)

# 9
arr2D = eval(input())

result = []
for i in range(len(arr2D)):
    max = 0
    for j in range(len(arr2D)):
        if arr2D[i][j] > max:
            max = arr2D[i][j]
    result.append(max)
print(result)

# 10
arr2D = eval(input())
rows = len(arr2D)
cols = len (arr2D[0])
new= []
for col in range(cols):
    min = arr2D[0][col]
    for row in range(1, rows):
        if arr2D[row][col] < min:
            min =arr2D[row][col]
    new.append(min)
print(new)

# 11
arr2D = eval(input())


result =[]
for i in range(len(arr2D)):
    sum = 0
    for j in range(len(arr2D[i])):
        sum += arr2D[i][j]
    result.append(sum)
print(result)

# 12
arr = eval(input())


sum_odd = 0
count_odd = 0
for num in arr:
    if num % 2 != 0:
        sum_odd += num
        count_odd += 1
if count_odd > 0:
    average = sum_odd // count_odd
else:
    average = 0
    
print(average)

# 13
strings = str(input())
lenght = len(strings) - 1
for i in range(len(strings)):
    print(strings[lenght - i],end="")

# 14
text =input()

small_text = text.lower()
if "rady" in small_text:
    print("Yes")
else:
    print("No")

# 15
tech_names = eval(input())  
new_names = []

for name in tech_names:
    if name not in new_names:
        new_names.append(name)

print(" ".join(str(x) for x in new_names))