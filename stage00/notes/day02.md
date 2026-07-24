# 语法清单

- `# 文字`	一级标题（## 二级，最多六级）
- `- 文字`	无序列表项
- `1. 文字`	有序列表项
- `**文字**`	粗体 
- ``代码``	行内代码（像 ls 这样）
- 空一行	分段
- ```代码块``` ```加代码块
- `>` 引用文字
# 快捷键
- ctrl+s 保存 save
- ctrl+z 撤销 
- ctrl+f 查找 find
- ctrl+n 新建文件 new【新建文件夹】用文件树上的new folder
- ctrl+` 开关终端
# markdown的优势
- 纯文本，不过时
- Git 能追踪 Markdown 每一行的变化，但 .docx 这种二进制文件它只能报一句 "Binary files differ"
# git传远程仓库
- git init                                    # 初始化仓库（如果还没有）
- git add .                                   # 添加所有文件
- git commit -m "第一次提交"                    # 提交
- git remote add origin https://github.com/你的用户名/仓库名.git   # 关联远程仓库
- git push -u origin master                   # 推送到 GitHub
- origin是一个自由命名的仓库名称，可以是my-project，，，，
# 终端git commit操作
- git add .                           # 把所有修改加入暂存区
- git commit -m "写清楚你改了什么"      # 提交
- git push                            # 推送到 GitHub