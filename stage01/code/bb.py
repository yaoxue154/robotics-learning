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
            with open("students.json","r") as f:
                data=json.load(f)
        except FileNotFoundError:
            data=[]
        for d in data:
            stu=Student(d["name"],d["grade"])
            self.grade_book.append(stu)
            print(stu)
gg=GradeBook()
