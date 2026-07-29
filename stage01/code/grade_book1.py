students=[{"name": "Alice", "grade": 90}, {"name": "Bob", "grade": 85}, {"name": "Charlie", "grade": 92}]
while True:
    name=input("请输入学生姓名(输入q退出): ")
    if name=="q":
        break
    elif name=="":
        print("姓名不能为空")
    elif name not in (student['name'] for student in students):
        print("学生不存在")
    else:
        for student in students:
            if student['name']==name:
                print(f"{student['name']}:{student['grade']}")
