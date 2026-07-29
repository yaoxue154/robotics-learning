students=[{"name": "Alice", "grade": 90}, {"name": "Bob", "grade": 85}, {"name": "Charlie", "grade": 82}]
for student in students:
    print(f"{student['name']}:{student['grade']}")
total=sum(grades['grade'] for grades in students)
print(f"平均分为: {total/ len(students)}") 
best_grade=students[0]
for student in students:
    if student['grade']>best_grade['grade']:
        best_grade=student
print(f"最高分为:{best_grade['name']}:{best_grade['grade']}")