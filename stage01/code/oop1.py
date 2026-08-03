class Student:
    def is_pass(self):
        return self.grade>=60
    def __init__(self, name, grade):
        print("生产线启动！收到原料：", name, grade)
        self.name = name
        self.grade = grade
        print("造好了，肚子里是：", self.__dict__)
alice=Student("Alice",85) # alice就是self
bob=Student("Bob",45)     # bob就是self
print(alice.name,alice.is_pass())
print(bob.name,bob.is_pass())
carol=Student("Carol",59)
print(carol.is_pass())
carol.grade=60
print(carol.is_pass())
