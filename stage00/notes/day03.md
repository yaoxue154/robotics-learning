# diff三态
## 工作区
- 编辑区域，每出现修改工作区都更新
## 暂存区
- 上一次`git add`的代码区
## 仓库
- 上一次`git commit`的代码区
### 关系
- 工作区add提交后，暂存区更新状态成add时工作区的状态
- 暂存区commit后，仓库变成暂存区的状态 
# diff指令
- `git diff` 查看工作区和暂存区的区别
- `git diff --staged` 查看暂存区和上一次commit的区别
# 后悔两档
- `git restore` 撤回add的内容的同时丢掉add修改的内容，直接将工作区的状态变回仓库【上一次commit】状态，丢失所有修改
- `git restore --staged`将add的内容撤回使得暂存区变回原来的暂存区，工作区修改保留
# 隔离网
- 在根目录下创建.gitignore文件，在文件中输入不需要让git管理的文件和内容，git就不再处理写入的相应内容
- git status 管理git的状态，功能类似于终端的ls