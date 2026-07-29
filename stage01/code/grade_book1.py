students=[{"name": "Alice", "grade": 90}, {"name": "Bob", "grade": 85}, {"name": "Charlie", "grade": 92}]
while True:
    name=input("请输入学生姓名(输入q退出): ")
    if name=="q":
        break
    elif name=="":
        print("姓名不能为空")
        continue
    found=False
    for student in students:
        if student['name']==name:
            found=True
            print(f"学生姓名: {student['name']}, 学生成绩: {student['grade']}")
    if not found:
         print("学生不存在") 