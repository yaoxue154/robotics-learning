# 第五课 列表与字典——装下整个班的成绩
## 第一容器：列表（list）——有序的队列
- scores = [85, 92, 78, 90, 66]
- 方括号围起来，逗号分隔，有顺序。词源：list，清单
## 索引（index）——按位置取货
- scores[0]     # 85 —— 第一个！从 0 开始数（range 的老规矩）
- scores[2]     # 78
- scores[-1]    # 66 —— 负数从队尾倒数，-1 是最后一个
- 取超出范围的位置会撞见 IndexError（索引越界）
## 遍历——for 循环真正的主场
```
for score in scores:
    print(score) 
```
- 每一个score里的量都会循环执行下面的命令，得到：
```
85
92
78
90
66
```
## append
- 队列会变：scores.append(88)（append 附加，加到队尾）、scores[0] = 100（按位置改）、len(scores)（队列长度）
- 统计四件套：len() 个数、sum() 总和、max() 最大、min() 最小——平均分就是 sum(scores) / len(scores)
## 第二容器：字典（dict）——带标签的抽屉
- 列表按位置找东西，字典按名字找：
```student = {"name": "张三", "score": 85}```
- 词源：dictionary，查字典——查"词条"（key，键）得到"释义"（value，值）。花括号，键: 值 一对对。

```student["name"]```      # "张三" —— 按键取值,键是student["name"]值是回车后取得的释义

```student["age"] = 18```  # 键不存在就新增，存在就改
- ⚠️ 查不存在的键会撞见 KeyError——第六种报错。
## 组合拳：列表装字典 = 小数据库
- 示例：
```
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
]
```
- 列表负责"排成队"，字典负责"每条数据带标签