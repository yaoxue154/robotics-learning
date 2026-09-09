import numpy as np
def my_matmul(A,B):
    C=[]
    for i in range(len(A)):
        new_row=[]
        for j in range(len(B[0])):
            total=0
            for k in range(len(B)):
                total+=A[i][k]*B[k][j]
            new_row.append(total)
        C.append(new_row)
    return C
R=([[0,-1],
    [1,0],
    [1,2]])
M=([[1,2,2],
    [3,4,4]])
print(my_matmul(R,M))
print(np.array(R)@np.array(M))
