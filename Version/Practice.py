students = [
    {"name":"Sok", "score":85},
    {"name":"Dara", "score":42},
    {"name":"Rith", "score":73},
    {"name":"Sophy", "score":35},
    {"name":"Mony", "score":90},
]
studentPassexams = []
for student in students:
    if student['score'] >= 60:
        studentPassexams.append(student['name'])
print(studentPassexams)