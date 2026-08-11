# 阶段 1 结业项目：成绩管理系统 v4
## 取最大
```
# 对象版：lambda 里用 .属性
best = max(objs, key=lambda s: s.grade)

# 字典版：lambda 里用 ["键"]，其他一字不差
best = max(dicts, key=lambda s: s["grade"])
print(best["name"], best["grade"])
```
## 概念改正
- __init__下的函数只在造对象的时候触发，对于成绩系统v5来言，只有grade_book=Gradebook()时触发，在对象.函数时是不会触发的。