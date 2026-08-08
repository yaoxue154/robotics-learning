import json
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def is_pass(self):
        return self.grade>=60
class GradeBook:
    def __init__(self):
        self.grade_book=[]
        try:
            with open("students.json","r",encoding="utf-8") as f:
                data=json.load(f)
        except FileNotFoundError:
            data=[]
        for d in data:
            stu=Student(d["name"],d["grade"])
            self.grade_book.append(stu)
    def save_and_exit(self):
        data=[]
        for stu in self.grade_book:
            data.append({"name":stu.name,"grade":stu.grade})
        with open("students.json","w",encoding="utf-8") as f:
            json.dump(data,f,indent=4)
    def add_student(self,name,grade):
            stu=Student(name,grade)
            self.grade_book.append(stu)
    def find(self,name):
        for student in self.grade_book:
            if student.name==name:
                return student
        return None
    def show_all_students(self):
        for stu in self.grade_book:
            if stu.is_pass():
                 print(f"name:{stu.name},grade:{stu.grade},status:pass")
            else:
                 print(f"name:{stu.name},grade:{stu.grade},status:fail")

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
            name=input("enter student name:")
            grade=float(input("enter student grade:"))
            grade_system.add_student(name,grade)
        except ValueError:
            print("invalid grade.please enter a valid number.")
    elif choice=="3":
        student_found=grade_system.find(input("enter student name:"))
        if student_found is not None:
            print(f"name:{student_found.name},grade:{student_found.grade}")
        else:
            print(f"student not found.")
    elif choice=="4":
        grade_system.save_and_exit()
        print("grade book saved.exiting.")
        break