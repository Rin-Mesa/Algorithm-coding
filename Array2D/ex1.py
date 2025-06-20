# array2D = [ [12, 3, 19, 0, 7],
#             [8, 14, 6, 2, 17],
#             [11, 20, 1, 13, 9],
#             [4, 10, 5, 18, 16],
#             [0, 15, 3, 19, 6]
#             ]
# newArr = []
# for arr in array2D:
#     sum = 0
#     for array in arr:
#         sum += array
#     newArr.append(sum)
# print(newArr)



array2D = [ [2, 3, 9, 0, 7],
            [8, 4, 6, 2, 1],
            [1, 2, 1, 1, 9],
            [4, 1, 5, 8, 6],
            [9, 5, 3, 9, 6]
            ]
for row in range(len(array2D)):
    for col in range(len(array2D[row])):
        if row + col == len(array2D)-1:
            value = "*"
        else:
            value = array2D[row][col]
        print(value, end=" " )
    print()

# array2D = [ [2, 3, 9, 0, 7],
#             [8, 4, 6, 2, 1],
#             [1, 2, 1, 1, 9],
#             [4, 1, 5, 8, 6],
#             [9, 5, 3, 9, 6]
#             ]
# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if col != row:
#             value = "*"
#         else:
#             value = array2D[row][col]
#         print(value, end=" " )
#     print()




# array2D = [ [2, 3, 9, 0, 7],
#             [8, 4, 6, 2, 1],
#             [1, 2, 1, 1, 9],
#             [4, 1, 5, 8, 6],
#             [9, 5, 3, 9, 6]
#             ]
# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if col == row or row + col ==len(array2D) -1:
#             value = "*"
#         else:
#             value = array2D[row][col]
#         print(value, end=" " )
#     print()




