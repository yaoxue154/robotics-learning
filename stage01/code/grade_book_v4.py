import json
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

class Grade_book:
    def __init__(self):
        self.data=[]
        with open("students.json","r") as f:
            self.grade_book=json.load(f)
            for d in self.grade_book:
                self.data.append(Student(d["name"],d["grade"]))
    def save(self):
        self.updata=[]
        for s in self.data:
            self.updata.append({"name":s.name,"grade":s.grade})
        with open ("students.json","w") as f:
            json.dump(self.updata,f,indent=4)

grade_book=Grade_book()
while True:
    print("1.show all students")
    print("2.add stuednt")
    print("3.find student")
    print("4.delete student")
    print("5.compile statistcs")
    print("6.save and exit")
    choice=input("choose what you want to do:")
    if choice=="1":
        for student in grade_book.data:
            print(f"name:{student.name},grade:{student.grade}")
    elif choice=="2":
        try:
            student_added=Student(input("name of student added:"),float(input("grade of student added:")))
        except ValueError:
            print(" The wrong grade!")
    elif choice=="3":
        for student in grade_book.data:
            if student.name==input("the name of the one you wanna find:"):
                print(f"name:{student.name},grade{student.grade}")
            else:
                print("no the one found!")
    elif choice=="4":
        for student in grade_book.data:
            if student.name==input("the name of the one you wanna delete:"):
                print(f"name:{student.name},grade{student.grade}")
                choice2=input("ensure you want to delete(y/n):")
                if choice2=="y":
                    
            else:
                print("no the one found!")
    666,写了半天原来还是一坨。


                

            




