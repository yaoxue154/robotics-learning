# 第 7 课：文件读写与异常——程序的记忆
## 三种模式
- "r"	读（默认）	类似cat               read
- "w"	写——先清空再写	类似> 覆盖重定向   write
- "a"	追加——接在末尾写 类似>> 追加重定向 add
## JSON存取
- 存
```
import json

with open("students.json", "w") as f:
    json.dump(students, f)      # 存：对象 → 文本 → 文件
```
- 取
```
import json
with open("students.json", "r") as f:
    data = json.load(f)         # 读：文件 → 文本 → 对象
print(type(data))               # 还是 list！对象原样复活
```
- 需要使用存储的数据的时候就要取出来，取出来了就可以使用。
# try except
```
try:
    age = int(input("年龄："))
except ValueError:
    print("请输入数字！")
```
- 这样可以将报错处理，使得程序不会以外报错崩溃，以往解决报错的方式是消除报错，要想出对策，有时浪费时间。
## FileNotFoundError
- 没有找到文件