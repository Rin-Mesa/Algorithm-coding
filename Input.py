# Enter your code here. Read input from STDIN. Print output to STDOUT
# arr2D = eval(input())

arr2D = [
    [2,5,4],
    [2,3,6],
    [2,9,6]
]
result = []
for row in arr2D:
    count_maximun = 0
    for num in row:
        count_maximun += 1
    result.append(count_maximun)
print(result)

# result = []
# for i in range(len(arr2D)):
#     max = 0
#     for j in range(len(arr2D)):
#         if arr2D[i][j] > max:
#             max = arr2D[i][j]
#     result.append(max)
# print(result)