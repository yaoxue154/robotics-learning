import json
from datetime import datetime
from student import(Student)
import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
DATA_FILE=os.path.join(BASE_DIR,"students.json")
LOG_FILE=os.path.join(BASE_DIR,"grade_book.log")

class GradeBook:
    def __init__(self):
        self.grade_book=[]
        try:
            with open(DATA_FILE,"r",encoding="utf-8") as f:
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
        with open(DATA_FILE,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=4)
    def add_student(self,name,grade):
            if self.find(name)==None:     
                stu=Student(name,grade)
                self.grade_book.append(stu)
            else:
                 print("the student had existed,please delete him final.")
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
        with open(LOG_FILE,"a",encoding="utf-8") as f:
                        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}|{action}|{detail}\n")

       