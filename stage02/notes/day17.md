# 第 12 课《Matplotlib——让数据长眼睛》
## pip 安装
- 格式1：python -m pip+工具名（安装到环境变量下设置的路径）（+ -i + 镜像地址，从镜像地址安装）
- 格式2：路径 + -m pip 加工具名（指定路径安装）
## matplotlib
- 示例1：
```
import matplotlib.pyplot as plt
import numpy as np

grades = np.array([85, 90, 78, 92, 88, 59])

plt.plot(grades, marker="o")                    # 折线图，每个数据点画个圆点
plt.axhline(60, color="red", linestyle="--")    # 一条横在 60 分的红色虚线：及格线
plt.title("class grades")                       # 标题（先用英文，中文有坑，下面讲）
plt.xlabel("student index")                     # x 轴标签
plt.ylabel("grade")                             # y 轴标签
plt.show()                                      # 亮相：弹出窗口
```
用法参照示例，工具的使用似乎不同于从头开始编写的代码，可能因为本身更加人性化的设计，使用时更多凭借一种感觉，不必计较那么多
- 示例2：
```
R = np.array([[0, -1], [1, 0]])    # 昨天那张 90° 搬迁公告
p = np.array([1.0, 0.0])           # 起点：正右
p2 = R @ p                         # 转完

plt.quiver(0, 0, p[0], p[1], angles="xy", scale_units="xy", scale=1, color="blue")   # 蓝箭头：转之前
plt.quiver(0, 0, p2[0], p2[1], angles="xy", scale_units="xy", scale=1, color="red")  # 红箭头：转之后
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.show()
```
- quiver是箭头（英译）
- 0，0是原点坐标
- p【0】是索引