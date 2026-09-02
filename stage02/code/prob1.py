import numpy as np
import matplotlib.pyplot as plt
coins=np.random.randint(0,2,size=(10000,3))
heads_per_group=np.sum(coins,axis=1)
all_heads=(heads_per_group==3)

print(f"投掷10000次,3枚硬币全是正面朝上的概率为:{all_heads.mean()}")
for n in [10,1000,10000]:
    flips=np.random.randint(0,2,size=n)
    print(f"投掷{n}次，正面朝上的概率为{flips.mean()}")

noise=np.random.normal(0,1,size=100000)
plt.hist(noise,bins=50)
plt.show() 



