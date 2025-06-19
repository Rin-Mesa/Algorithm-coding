fruits = [
    {"name":"Aplle","qty":2, "price":20},
    {"name":"Banana","qty":0, "price":30},
    {"name":"Pine Aplle","qty":0, "price":40},
    {"name":"Wood Aplle","qty":2, "price":10},
]

# Q1 Display the fruit out of stock
# arrayFruit = []
# for fruit in fruits:
#     if fruit["qty"] == 0:
#         arrayFruit.append(fruit['name'])
# print(arrayFruit)

# # Q2 list the fruit that has price <= 20
# fruitPrice = []
# for i in range(len(fruits)):
#     if fruits[i]["price"] <= 20:
#         fruitPrice.append(fruits[i]['name'])
# print(fruitPrice)

# 1 way
# Q3 add 5 to qty who has qty == 0
# new_array = []
# for fruit in fruits:
#     if fruit["qty"] == 0:
#         fruit["qty"] += 5
#         new_array.append(fruit)
#     else:
#         new_array.append(fruit)
# print(new_array)

# 2nd way 
# for i in range(len(fruits)):
#     if fruits[i]["qty"] == 0:
#         fruits[i]["qty"] = 5
# print(fruits)


# for fruit in fruits:
#     if fruit['qty'] == 0:
#         fruit["qty"] += 5
#         print(fruit)
#     else:
#         print(fruit)