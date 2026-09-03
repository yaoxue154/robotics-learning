import numpy as np
import matplotlib.pyplot as plt

truth=2.0
noise=np.random.normal(0,0.3,100)
readings=truth+noise
plt.plot(readings,'o')
plt.axhline(y=truth,color='r',label='truth')
plt.ylim(0,4)
plt.legend()
plt.show()

estimate=np.mean(readings)
print(readings[0])
print(estimate)
print(truth)
print(readings[0]-truth)
print(estimate-truth)  

t=np.arange(0,10,0.1)
truth=2+t*0.5
readings=truth+noise
fliters=[]
for i in range(5,len(readings)-5):
    windows=readings[i-5:i+6]
    fliters.append(windows.mean())
plt.plot(t[0:6],readings[0:6],'o',label='unseen')
plt.plot(t[-5:],readings[-5:],'o',label='unseen')
plt.plot(t[5:-5],fliters,'r',label='flitered')
plt.plot(t,readings,'g',label='original_noise_data',marker='o')
plt.plot(t,truth,'k',label='truth')
plt.legend()
plt.show()




