# __file__
- 示例：
```
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# __file__            → Python 自动给的变量：这个 .py 文件自己的路径
# os.path.abspath()   → 补全成绝对路径（不管你站在哪跑）
# os.path.dirname()   → 只留文件夹部分
# 结果：BASE_DIR = stage01/code/final（这个文件的家）

DATA_FILE = os.path.join(BASE_DIR, "students.json")
LOG_FILE = os.path.join(BASE_DIR, "grade_book.log")
```
- 看着复杂，实际上就是实现了一个功能：
1. 获得程序的路径（家）
2. 规定数据文件的路径
- 这些就是站位的固定
#  join 得到的是什么？
- 是一个字符串，字符串里包着数据文件的决对路径
```
DATA_FILE = os.path.join(BASE_DIR, "students.json")
# DATA_FILE 的内容就是一行文本：
# "F:\Vibecoding project\item2 learning\stage01\code\final\students.json"
```


