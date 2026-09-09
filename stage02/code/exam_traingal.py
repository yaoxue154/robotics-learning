import numpy as np
import matplotlib.pyplot as plt
O=np.array([[0,2,1],
            [0,0,1.5]])
R=np.array([[0,-1],
            [1,0]])
P=R@O

Ox=O[0]
fx=O[0,0]
Oy=O[1]
fy=O[1,0]
ox=list(Ox)+[fx]
oy=list(Oy)+[fy]
plt.plot(ox,oy,'b')

Px=P[0]
fxc=P[0,0]
Py=P[1]
fyc=P[1,0]
px=list(Px)+[fxc]
py=list(Py)+[fyc]
plt.plot(px,py,'r')
plt.axis('equal')
plt.show()