# # input arr : [1,2,3,4]
# iuput arr : ['a','b','c','d']
# input : []
# arr = eval(input('Enter your Array: '))
# if arr == []:
#     print('There is not element!')
# else:
#     new=[]
#     for i in range(len(arr)):
#         new.append(arr[len(arr)-i-1])
#     print(new)


# input year month and day 
# year = (input('Enter your year:'))
# month = (input('Enter your month: '))
# day = (input('Enter your day:'))

# date_info = {
#     'year': int(year),
#     'month': month,
#     'day': int(day)
# }

# print(date_info)


# # input your arr
# arr = eval(input('Enter your arr: '))
# if len(arr) == 0:
#     print('There is not elemant!')
# else:
#     new = []
#     for item in arr:
#         if item not in new:
#             new.append(item)
#     print(new)


# stocks = [
#     {'name': 'computer', 'price':{'value': 500, 'currency': 'USD'}},
#     {'name': 'banana', 'price':{'value': 1000, 'currency': 'Riel'}},
#     {'name': 'coconut', 'price':{'value': 3500, 'currency': 'Riel'}},
#     {'name': 'motobike', 'price':{'value': 2300, 'currency': 'USD'}},
# ]


# total_Riel = 0
# total_USD = 0
# for stock in stocks:
#     if stock['price']['currency'] == 'USD':
#         total_USD += stock['price']['value']
#     if stock['price']['currency'] == 'Riel':
#         total_Riel += stock['price']['value']
# print(total_USD,'USD')
# print(total_Riel,'Riel')


# array2D=[[9,4,5],[3,2,7],[6,3,5]]

# new = []
# for item in array2D:
#     sum = 0
#     for arr in item:
#         sum += arr
#     new.append(sum)
# print(new)



array2D=[[2,3,4],[0,1,2],[5,4,3]]
# array2D = eval(input('Enter your Array2D:'))
if len(array2D) == 0:
    print('There is not element!')
    new = []
    for item in array2D:
        sum = 0
        for arr in item:
            sum += arr
        new.append(sum)
    print(new)