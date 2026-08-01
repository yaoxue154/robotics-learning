import json
try:
    with open('students.json', 'r') as f:
        grade_book = json.load(f)
except FileNotFoundError:
    grade_book = {}
def find(name):
        for student in grade_book:
            if student["name"] == name:                 
                return student["grade"]
            else:
                return None

print(find("Bob"))