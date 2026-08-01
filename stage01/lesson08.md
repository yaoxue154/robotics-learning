# 第 8 课《面向对象——把数据和行为捆在一起》

> 教师教案 · 2026-08-02 开课 · 学员可预习概念，禁止照抄代码

## 开场（约 10 分钟）

回问旧账（答不上来回炉）：
1. 追加实验：`"a"` 模式连跑两遍 `my_write.py`，文件变成什么样？读回来什么结果？
2. 删除仪式三步走（阶段 0 老账）。
3. 快问：`json.dump` 认哪六种类型？

钩子：打开 `grade_book_v2.py`，现场指出三个痛点——
- 学生数据是字典，长什么样全靠记忆，拼错键名运行时才炸
- `find` 函数漂在外面，和它操作的数据分家住
- 谁都能直接改 `grade_book` 列表，没有门卫

## 第一部分：先看跑（约 15 分钟）

最小示例（教师先演示，学员再亲手敲）：

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_pass(self):
        return self.grade >= 60
```

跑：`alice = Student("Alice", 85)`，访问 `alice.name`，调用 `alice.is_pass()`。

拆解四个概念（每个都要生活类比）：
- `class` = 图纸 / 模具；对象 = 照图纸造出来的实体
- `__init__` = 出厂设置，造对象时自动跑一次
- `self` = "我自己"，每个对象拿自己的那份数据
- 方法 = 对象自己会做的事（对比：字典是哑巴只装数据，对象是活物）

## 第二部分：RoboMaster 钩子（约 10 分钟）

真实机器人的代码组织：底盘 `Chassis`、云台 `Gimbal`、发射机构 `Shooter` 各是一个类；每个电机是一个 `Motor` 对象，有自己的 `speed` 属性和 `set_speed()` 方法。

```python
class Motor:
    def __init__(self, motor_id):
        self.motor_id = motor_id
        self.speed = 0

    def set_speed(self, s):
        self.speed = s
```

点题：RoboMaster 的嵌入式代码（C++）和视觉代码（Python）全是这个骨架。学类，就是在学机器人代码的组织方式。

## 第三部分：动手——成绩簿重构为面向对象（主体）

`grade_book_v3.py`，功能与 v2 完全一致（菜单 1查看 2添加 3查询 4保存退出），`students.json` 格式不变。

注释先行法骨架（教师给注释，学员填代码）：

```python
# class Student：属性 name、grade；方法 is_pass()
# class GradeBook：内部装 Student 对象列表
#   方法：load() 读文件 / save() 写文件 / add() / find() / show_all()
# 主循环：菜单与 v2 相同
```

预设难点（卡 30 分钟再给提示）：`json.dump` 不吃自定义对象，save 时必须把 Student 对象翻回字典。提示方向：循环或列表推导，手工拼 `{"name": ..., "grade": ...}`。

## 作业清单

- [ ] `stage01/code/grade_book_v3.py` 四项功能全通，数据文件与 v2 兼容
- [ ] `stage01/notes/day11.md`：class / 对象 / `__init__` / `self` 四概念各一句话 + 一个自己的生活类比
- [ ] 思考题（抽查）：`json.dump(student)` 为什么报错？你怎么解决的？
- [ ] 老规矩：commit + push 后喊验收

## 验收点（教师用）

- 四项功能实测全过；`students.json` 格式未变
- 能逐行讲清 `__init__` 和 `self`
- 对象→字典的转换代码是亲手所写，能讲清
- commit message 如实概括
