# 第 8 课《面向对象——把数据和行为捆在一起》
## __init__(self,...,....)函数
示例：
```
class Student:                          # ① 图纸：声明"学生"这种东西长什么样
    def __init__(self, name, grade):    # ② 生产线：每造一个学生，自动跑一次
        self.name = name                # ③ 把传入的名字，贴在"我自己"身上
        self.grade = grade

    def is_pass(self):                  # ④ 图纸上写的"会做的事"
        return self.grade >= 60
```
- 每一次调用Student（name,grade）都会自动运行__init__下的内容
## self
- 沿用示例
- 有```person1=Student(Bob,100)```,就会自动调用init，此时self就是person1，person1.name=Bob，person2.grade=100
- 调用函数时，都是self.def(函数名称如```self.find()```)才可以调用，不是find（name）了,不过find(name)没有失效，还是可以使用的
- 产生的目的是解决变量被指定，导致无法解决多个对象需要使用同一个函数的问题，一个变量被赋值，后续操作都会发生在该变量上，如果是self.变量，self是多变的，同一个变量使用的可能性就会增加“ Python 需要一个占位符，意思是"将来谁调用我，就指谁"。这个占位符就是 self——它的意思是"我" Python 需要一个占位符，意思是"将来谁调用我，就指谁"。这个占位符就是 self——它的意思是"我"：”例子：“gb.save() 存成绩，g.save() 存游戏进度”
## class
- 函数是把一些处理操作简化汇聚变成一个小盒子，方便调用。class是把函数们归类，变成一个大盒子，方便辨认和管理，是一个函数组。


