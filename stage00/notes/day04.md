# 远程仓库四步
1. github建仓库 本地如果有项目历史，不要勾选 README、.gitignore、License
2. 本地远程关联
- git remote add origin https://github.com/yaoxue154/robotics-learning.git
- git remote -v    # 验证：能看到 origin 对应的两行地址
3. 推送到远程仓库 
- git push -u origin master[后续可以直接`git push`]
4. 网页验证
- 刷新仓库页面，检查是否推送成功
# 词源
- emote（远程的）、push（推）、pull（拉）、clone（克隆）、origin（源头——远程仓库的默认别名）
- upstream（上游）：本地分支和远程分支的绑定关系，push -u 就是建立这条"航道"，建好之后以后只敲 git push 就行
# 踩坑
- github仓库名不支持中文，写入中文会自动变为-