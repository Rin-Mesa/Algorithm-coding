students = [
    {"name":"Sok", "score":85},
    {"name":"Dara", "score":42},
    {"name":"Rith", "score":73},
    {"name":"Sophy", "score":35},
    {"name":"Mony", "score":90},
    ]
name = input("Enter student's name:")
for student in students:
    if name == student['name']:
        print(f"{student['name']}'s score is {student['score']}")