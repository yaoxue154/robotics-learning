import numpy as np
grades=np.array([85,90,78,92,7,59])
print("平均：", grades.mean())
print("最高：", grades.max())
print("最低：", grades.min())
print("标准差：", grades.std())
print("不及格",grades[grades<60])
