import matplotlib.pyplot as plt
import numpy as np

R = np.array([[0, -1], [1, 0]])    
p = np.array([1.0, 0.0])          
p2 = R @ p                         

plt.quiver(0, 0, p[0], p[1], angles="xy",scale_units="xy", scale=1, color="blue")   
plt.quiver(0, 0, p2[0], p2[1], angles="xy", scale_units="xy", scale=1, color="red") 
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.show()