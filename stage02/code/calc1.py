import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,5,0.1)
pos=t**2+20

vel=np.diff(pos)/0.1
vel_back=np.cumsum(vel)*0.1
plt.plot(t,pos,label="position")
plt.plot(t[1:],vel,label="velocity")
plt.plot(t[1:],vel_back,label="velocity_back")

plt.legend()
plt.show()

