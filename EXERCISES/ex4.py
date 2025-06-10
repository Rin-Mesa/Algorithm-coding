students = [
    {"name":"Sok", "score":85},
    {"name":"Dara", "score":42},
    {"name":"Rith", "score":73},
    {"name":"Sophy", "score":35},
    {"name":"Mony", "score":90},
    ]
max = 0
for i in range(len(students)):
    if students[i]["score"] > max:
        max = students[i]["score"]
print(f"{students[i]['name']} with score {students[i]['score']}")