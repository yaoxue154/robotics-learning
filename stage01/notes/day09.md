# 第六课 函数——代码的积木
## def
- 词源：define，定义（一个函数）--打造一个盒子
- 示例：
```
def cheer():
    print("加油！")
    print("你能行！")

cheer()
```
得到
```
加油
 
你能行
```
- 其中输入的cheer()就是调用该函数的命令
## 参数
- 参数——盒子的入口
```
def greet(name):
    print(f"你好，{name}！")

greet("张三")    # 你好，张三！
greet("李四")    # 你好，李四！
```
- 括号里的 name 叫参数（parameter）——盒子的"投入口",参数由你的输入来绝对，是可变的。
## return
- 示例：
```
def add(a, b):
    return a + b

result = add(3, 5)
print(result)    
```
- 得到：
```
8
```
- return后就得到a+b的值，但是这个值在哪里，怎么获得呢？函数add(a,b)就是这个值所以result = add(3, 5)，result==8
# print和return的区别
- print是输出
- return是返回结果，可交给程序使用，print是输出给用户看的
