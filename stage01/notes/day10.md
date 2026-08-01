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
## 追加三步走
- 从json中取出列表 read
- append加内容到列表里 加
- json.dump写入覆盖 write
## a的应用场景
- 因为写入后，之前的列表和追加的内容直接缝在一起，会导致结构出现异常“为什么追加会毁掉 JSON？ 因为一份 JSON 文件整体是一个结构——外面那对 [ ] 或 { } 是包装袋。追加等于把两个包装袋缝在一起，机器拆开一看：两个货，不知道哪个是正的，拒收。”所以“那 "a" 模式什么时候是对的？ 写日志。日志没有包装袋，每行独立：

with open("scratch/robot.log", "a") as f:
    f.write("2026-08-01 20:30 电机启动\n")
这段连跑三遍，文件里就是三行，互不干扰。机器人跑起来的时候，传感器数据、报错信息就是这么一行行追加上去的——事后翻日志查故障，全靠它。”