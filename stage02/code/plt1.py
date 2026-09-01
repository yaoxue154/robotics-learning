import matplotlib.pyplot as plt
import numpy as np

grades=np.array([85,90,78,92,88,59])
plt.plot(grades,marker="o")
plt.axhline(60,color="red",linestyle="--")
plt.title("class grades")
plt.xlabel("student index")
plt.ylabel("grade")
plt.show()