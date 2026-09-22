# 交接文档 · 换机指南

> 用途：换电脑后，照着本文档恢复全部学习环境并继续课程。
> 最近更新：2026-09-22（军训顺延开发板实战；新增目标：12 月前导师双选冲徐立明组，小车后追加机械臂项目）

## 一、课程当前状态

- 阶段 0 筑基 ✅ / 阶段 1 Python 与编程思维 ✅ / 阶段 2 数学与科学计算 ✅
- **下一课：阶段 3 第 16 课——C 语言登场（装 gcc、编译概念、第一个 C 程序）**（军训结束后开）
- 12 月前：导师双选，目标徐立明组；双选前要攒出"小车 + 机械臂"两件实物作品
- 详细进度见 `PROGRESS.md`（每次开课教师先读它）

## 二、要搬走的东西

| 物品 | 位置 | 必须？ |
|---|---|---|
| 课程仓库（整个文件夹，**含 `.git` 隐藏目录**） | `F:\Vibecoding project\item2 learning` | ✅ 必须 |
| Kimi Code 会话与配置 | `C:\Users\Administrator\.kimi-code\` | 可选（不搬则新会话靠 PROGRESS.md 接力） |

注意：GitHub 是云端兜底，但 `git clone` **拿不回**被忽略的文件（`scratch/` 游乐场、各 `students.json`、日志）——所以整机拷贝优先，clone 只作备用方案。

## 三、新电脑要装的软件

1. **Git**（含 Git Bash）
2. **Python 3.14**（勾选 Add to PATH；认准用 `py` 启动器——`python` 命令可能是微软商店诱饵 stub，踩过一次）
3. **VS Code**
4. **Kimi Code CLI**
5. 第三方库：`py -m pip install numpy matplotlib`（装不上先换源/回官方源）

## 四、恢复后验收清单（新机器第一课先跑这个）

```bash
py --version                    # 应显示 3.14.x
py -c "import numpy, matplotlib"   # 不报错即可
cd "项目目录" && git log --oneline -3   # 应看到完整历史
git status -sb                  # 应与 origin/master 同步
```

## 五、硬性约定（开学即恢复执行）

- 三条铁规：代码亲手敲 / 卡 30 分钟再问 / 不懂就说不懂
- 提交节奏：本地 commit 随时做，验收通过后统一 push（加速器切网会断会话）
- 演示代码结构化排版、括号密集处加空格（终端渲染坑）
- 跑中文脚本：`py -X utf8 文件.py`（新机器上 `python` 是诱饵）
- 详见 `SYLLABUS.md` 教学约定一节

## 六、防丢确认

- [ ] 老机器：所有改动 commit + push 完毕（`git status` 干净、无 ahead）
- [ ] 整个文件夹已拷贝（含 `.git`）
- [ ] （可选）`.kimi-code` 已拷贝
- [ ] 新机器四步验收清单全绿
