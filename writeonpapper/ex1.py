# EXERCISE 01
# # Enter your object:{"2022A":20, "2023B":30, "2023C":25} 
my_dict = eval(input("Enter your object:"))
if len(my_dict) == 0:
    print("No asigned")
else:
     for key in my_dict:
        print("Numbers of student in class", key, "is", my_dict[key]) 

# EXERCISE 02
# Result = 9750
# materiles = [
#     {'name':'Computer','quantity':20, 'retail_price':400, 'quality':'Good'},
#     {'name':'Computer','quantity':10, 'retail_price':200, 'quality':'Not Good'},
#     {'name':'Moniter','quantity':20, 'retail_price':1000, 'quality':'Not Good'},
#     {'name':'Keyboard','quantity':10, 'retail_price':150, 'quality':'Good'},
#     {'name':'Speaker','quantity':5, 'retail_price':50, 'quality':'Good'},
# ]

# total = 0
# for materile in materiles:
#     if materile['quality'] == 'Good':
#         total += materile['retail_price'] * materile['quantity']
# print(total)


# EXERCISE 03
# students = [
#     {'name': 'Him', 'class': 'A', 'score': 70},
#     {'name': 'Rady', 'class': 'B', 'score': 80},
# ]
# print(type(students))
# print(type(students[1]))
# print(type(students[0]['name']))
# print(type(students[0]['class']))
# print(type(students[0]['score']))


students = [
    {'name': 'HIM', 'class': 'A', 'score': 90},
    {'name': 'Bopha', 'class': 'A', 'score': 40},
    {'name': 'Tesla', 'class': 'A', 'score': 80},
    {'name': 'Kunthea', 'class': 'B', 'score': 100},
    {'name': 'Kolap', 'class': 'B', 'score': 90},
    {'name': 'Vanna', 'class': 'B', 'score': 70},
    {'name': 'Chompey', 'class': 'C', 'score': 50},
    {'name': 'Romchong', 'class': 'C', 'score': 90},
]

for item in students:
    if item["score"] <= 40:
        print(students)
