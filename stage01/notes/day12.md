# 对象与字典的区别
## 容器
- 对象的容器和字典的容器都是列表
## 使用
- 字典可以直接使用，从json文件中读出，再用列表名加键来找值如"student["name"]
- 对象需要一个转换：

json读出字典，先建立一个空列表，再用任意一个变量=定义的大函数名（），最后append写入变量，可见grade_book_v3.py,Grade下的__init__,空列表里的内容就变成了对象，根据大函数对对象的参数设置，来决定引用对象的参数的具体数值及方法
- 最后，对象还要重新再建一个空列表，用写字典的方式，将数据使用for循环重新写进去，如： 
```
def save_and_exit(self):
        data=[]
        for stu in self.grade_book:
            data.append({"name":stu.name,"grade":stu.grade})
        with open("students.json","w") as f:
            json.dump(data,f,indent=4)
```
- 另外，使用时也变成了对象.name或者对象.grade这样的格式，而其他的使用方法则和字典的一样，需要取用时，用到for循环，循环装对象的那个列表
- 仓库是列表，不会变。而字典和对象是住户，有区别，都可以住仓库。
# 记得 列表.append（"name"：名字）吗
- “列表”就是python自带的一个类（图纸），不用重新定义，但是像```grade_system.add_student(name,grade)```这样的就需要定义grade_system这个类（图纸）
- 取到什么样的对象，就可以直接使用该对象对应的类下的函数