import json
from datetime import datetime
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
    def remove_student(self,name):       
        if not self.find(name):
            print("no the one found!")
        else:
            student=self.find(name)
            print(f"{student.name}:{student.grade}")
            choice1=input("ensure you want to dalete this student(y/n):")
            if choice1=="y":
                self.grade_book.remove(student)
                print("deleted!")
                self.log("DELETE",name)
            else:
                print("cancelde!")
    def show_stats(self):
        if not self.grade_book:
            print("暂无数据")
            return
        grade=[]
        for stu in self.grade_book:
            grade.append(stu.grade)
        passed_student=0
        for s in self.grade_book:
            if s.is_pass():
                passed_student=passed_student+1            
        headcount=len(self.grade_book)
        total_grade=sum(grade)
        best=max(self.grade_book,key=lambda s:s.grade)
        lowest=min(self.grade_book,key=lambda s:s.grade)
        print(f"headcount:{headcount}")
        print(f"averagr grade:{total_grade/headcount}")
        print(f"best student is {best.name},grade:{best.grade}")
        print(f"lowest grade:{lowest.grade}")  # 保护学生自尊心，不披露名字
        print(f"pass rate:{passed_student/headcount}")

    def log(self,action,detail):
        with open("scratch/grade_book.log","a",encoding="utf-8") as f:
                        f.write(f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}|{action}|{detail}\n")

grade_system=GradeBook()
while True:
    print("grade book menu:")
    print("1.view all students")
    print("2.add student")
    print("3.find student")
    print("4.save and exit")
    print("5.delete student")
    print("6.show stats")
    choice=input("enter your choice(1-6):")
    if choice not in ["1","2","3","4","5","6"]:
        print("invalid choice.please enter a number between 1 and 6.")
        continue
    elif choice=="1":
        grade_system.show_all_students()
    elif choice=="2":
        try:
            name=input("enter student name:")
            grade=float(input("enter student grade:"))
            grade_system.add_student(name,grade)            
            grade_system.log("ADD",f"({name}:{grade})")
        except ValueError:
            print("invalid grade,please enter a valid number.")
    elif choice=="3":
        student_found=grade_system.find(input("enter student name:"))
        if student_found is not None:
            print(f"name:{student_found.name},grade:{student_found.grade}")
        else:
            print(f"student not found.")
    elif choice=="4":
        grade_system.save_and_exit()   
        print("grade book saved.exiting.")
        grade_system.log("SAVE",f"(total headcount:{len(grade_system.grade_book)})")
        break
    elif choice=="5":
        name=input("enter the student name:")
        grade_system.remove_student(name)
    elif choice=="6":
        grade_system.show_stats()
        
    