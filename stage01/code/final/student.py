class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def is_pass(self):
        return self.grade>=60