# 结业测试plt三角形旋转
## 注意点
- list（）对于一个数字如list（9）时会报错所以用【9】
- 列表加列表，结果是列表，如【11，1】+【1】=【11，1，1】
- 那么，怎么往列表里面加列表呢，绝对不是【】+【】，用append，可见于矩阵乘法的本质处写下的代码。示例：
```
c=[]
b=[1,3]
g=[1,6]
c.append(b)
c.append(g)
print(c)
```
- append是一个函数，它的放回值是none
所以c = c.append(g)   # c 变成了 None

   c = c.append(y)   # 报错！None 没有 append 方法
