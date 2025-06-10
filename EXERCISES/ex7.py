students = [
    {"name":"Sok", "score":85},
    {"name":"Dara", "score":42},
    {"name":"Rith", "score":73},
    {"name":"Sophy", "score":35},
    {"name":"Mony", "score":90},
]
for i in range(len(students)):
    max_index = i
    for j in range(i + 1, len(students)):
        if students[j]["score"] > students[max_index]["score"]:
            max_index = j
    students[i], students[max_index] = students[max_index], students[i]
for student in students:
    print(f"{student['name']}, ", end='')