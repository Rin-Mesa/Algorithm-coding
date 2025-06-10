studnets = [
    {"name":"Sok", "score":85},
    {"name":"Dara", "score":42},
    {"name":"Rith", "score":73},
    {"name":"Sophy", "score":35},
    {"name":"Mony", "score":90},
    ]
for i in range(len(studnets)):
    if studnets[i]["score"]> 50:
        print(studnets[i]["name"])