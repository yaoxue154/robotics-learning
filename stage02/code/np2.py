import numpy as np
grades=np.array([[89,22,67],
                 [97,79,90],
                 [69,87,70],
                 [87,98,58],
                 [70,80,40],
                 [80,90,60]])
print(grades.shape)
print(grades[5,1])
print(grades[:,0])
print(grades.mean(axis=0))
print(grades.mean(axis=1))
grades=grades+5
print(grades.shape)
print(grades[5,1])
print(grades[:,0])
print(grades.mean(axis=0))
print(grades.mean(axis=1))