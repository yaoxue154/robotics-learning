import json
try:
    with open('students.json', 'r') as f:
        grade_book = json.load(f)
except FileNotFoundError:
    grade_book = []
def find(name):
        for student in grade_book:
            if student["name"] == name:                 
                return student["grade"]
        return None
while True:
    print("Grade Book Menu:")
    print("1. view the all students")
    print("2. Add Student")
    print("3. View Students")
    print("4. Save and Exit")
    choice = input("Enter your choice (1-4): ")
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please enter a number between 1 and 4.")
        continue
    elif choice == "1":
        for student in grade_book:
            print(f"Name: {student['name']}, Grade: {student['grade']}")
    elif choice == "2":
        name = (input("add student name: "))
        grade =(input("add student grade: "))
        try:
            grade_book.append({"name": name, "grade": float(grade)})
        except ValueError:
            print(f"Error occurred while adding student")
    elif choice == "3":
        name = (input("Enter student name: "))
        grade = find(name)
        if grade is not None:
            print(f"Name: {name}, Grade: {grade}")
        else:
            print(f"Student {name} not found.")
    elif choice == "4":
        with open('students.json', 'w') as f:
            json.dump(grade_book, f, indent=4)
        print("Grade book saved. Exiting.")
        break