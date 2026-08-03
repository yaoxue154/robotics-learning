import json
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def is_pass(self):
        return self.grade>=60
class GradeBook:
    def __init__(self):
        try:
            with open("students.json","r") as f:
                self.grade_book=json.load(f)
        except FileNotFoundError:
            self.grade_book=[]
    def save_and_exit(self):
        with open("students.json","w") as f:
            json.dump(self.grade_book,f,indent=4)
    def add_student(self,name,grade):
        try:
            self.grade_book.append({"name":name,"grade":float(grade)})
        except ValueError:
            print(f"error occurred while adding student")
    def find(self,name):
        for student in self.grade_book:
            if student["name"]==name:
                return student["grade"]
        return None
    def show_all_students(self):
        for student in self.grade_book:
            print(f"name:{student['name']},grade:{student['grade']}")


grade_system=GradeBook()
while True:
    print("grade book menu:")
    print("1.view all students")
    print("2.add student")
    print("3.find student")
    print("4.save and exit")
    choice=input("enter your choice(1-4):")
    if choice not in ["1","2","3","4"]:
        print("invalid choice.please enter a number between 1 and 4.")
        continue
    elif choice=="1":
        grade_system.show_all_students()
    elif choice=="2":
        try:
            student_added=Student(input("add student name:"),float(input("add student grade:")))
            grade_system.add_student(student_added.name,student_added.grade)
        except ValueError:
            print("invalid grade.please enter a valid number.")
    elif choice=="3":
        student_found=Student(input("enter student name:"),0)
        student_found.grade=grade_system.find(student_found.name)
        if student_found is not None:
            print(f"name:{student_found.name},grade:{student_found.grade}")
        else:
            print(f"student {student_found.name} not found.")
    elif choice=="4":
        grade_system.save_and_exit()
        print("grade book saved.exiting.")
        break