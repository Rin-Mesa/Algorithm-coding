students = [
    {"name": "Sok", "score": 85},
    {"name": "Dara", "score": 42},
    {"name": "Rith", "score": 73},
    {"name": "Sophy", "score": 35},
    {"name": "Mony", "score": 90},
]
scores = [student["score"] for student in students]
if len(scores) == len(set(scores)):
    print("No duplicates")
else:
    print("Duplicates found")
