# # [ {'name': 'banana', 'price': 1000, 'quantity': 2},{'name': 'mango', 'price': 2000, 'quantity': 1} ]
# # Result = 4000



# fruites = eval(input("Enter your oblect:"))
# total = 0
# for fruite in fruites:
#     total += fruite['price'] * fruite['quantity']
# print(total)



# # Q2
# fruits_meats = eval(input("Enter your oblect: "))
# fruits_cont = 0
# meats_cont = 0
# if len(fruits_meats)==0:
#     print("No result")
# else:
#     for item in fruits_meats:
#         for key in item:
#             if key  == "fruit":
#                 fruits_cont += 1
#             if key == 'meat':
#                 meats_cont += 1
# print('Fruite:', fruits_cont)
# print('meat:', meats_cont)

# 3
students = [
    {'name': 'Bunthoeun', 'score': 90},
    {'name': 'Kunthy', 'score': 75},
    {'name': 'Sreymom', 'score': 95},
]
# students = eval(input('Enter your student: '))
beast_student = students[0]['score']
higthest_score = students[0]['name']
all_students = True 
for item in students:
    if item['score'] > beast_student:
        higthest_score = item['score']
        beast_student = item['name']
    if item['score'] <= 75:
        all_student = False

print('The best student is', beast_student)
if all_students:
    print("ALL students have more than 75")


# students = eval(input("Enter name student: "))
# first = students[0]
# best_student = first["name"]
# best_score = first["score"]

# for student in students:
#     if student["score"] > best_score:
#         best_score = student["score"]
#         best_student = student["name"]

# print(f"The best student is {best_student}")