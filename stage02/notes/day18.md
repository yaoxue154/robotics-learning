# 第 14 课《概率基础——和不确定性打交道》
- 示例：
```
import numpy as np
import matplotlib.pyplot as plt

noise = np.random.normal(0, 1, size=10000)   # 均值0（不偏心）、标准差1（波动幅度）、一万个噪声点
plt.hist(noise, bins=50)                     # 直方图：分成 50 根柱子数人数
plt.show()
```
- hist直方图，bins————柱子数
- plot曲线图，marker————拐点形状
- quiver箭头图，（原点x，原点y，终点x，终点y）
- 示例：
```
heads_per_group=np.sum(coins,axis=1)
all_heads=(heads_per_group==3)
```
- all_heads得到的是一堆的false和true，false是0，true是1，所以，可以用sum处理all_heads