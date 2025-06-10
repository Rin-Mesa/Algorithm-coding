students = [
    {"name":"Sok", "score":85},
    {"name":"Dara", "score":42},
    {"name":"Rith", "score":73},
    {"name":"Sophy", "score":35},
    {"name":"Mony", "score":90},
]
name = "Rith"
for i in range(len(students)):
    if students[i]['name'] == name:
        print(f"{students[i]['name']}'s score {students[i]['score']}")
