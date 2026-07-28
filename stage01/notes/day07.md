# 第四课 循环——让程序不知疲倦
## 条件循环--while
示例：
```
count = 0
while count < 5:
    print(count)
    count = count + 1
```
### while三要素
- 初始值（count = 0）放到while之前，不然每次循环初始值都会变成一开始设定的0
- 条件（count < 5）True就循环属于while的内容，false就跳过属于while的内容
- 更新（count = count + 1）
- 注意:如果没有更新，whlie true下的命令会一直循环执行，进入死循环（ctrl+c退出，键盘中断）
## 计数循环--for range
示例：
```
for i in range(11):
    print(i**2)
```
- 词源 for（对于每一个）、range（范围）、iterate（迭代，重复逐步推进）
- range()不含终点，range(6)结果是0，1，2，3，4，5
- range是从零开始
## break和continue
- break（打破）：直接跳出整个循环——紧急出口
- continue（继续）：跳过本次剩余部分，直接进下一轮——这一站不停，所以是continue加要跳过的部分，跳过失效的部分会变灰（编辑器中）
## while true+break 结构
示例：
```
while True:          # 一直跑，永不停止
    x = input("输入内容（输入 q 退出）: ")
    if x == "q":
        break        # 遇到 q 就跳出去
    print(f"你输入了: {x}")
```