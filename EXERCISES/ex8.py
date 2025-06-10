students = [
    {"name":"Sok", "score":85},
    {"name":"Dara", "score":42},
    {"name":"Rith", "score":73},
    {"name":"Sophy", "score":35},
    {"name":"Mony", "score":90},
]
for student in students:
    student["score"] += 5
    print(f"{student['name']}: {student['score']}")
