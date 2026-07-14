import numpy as np

decide = int(input())
if decide == 0:
    A = np.array([[1,2],[3,4]])
    B = np.array([[4,3],[2,1]])
    C = A @ B
    print(C)
    D = A.T
    print(D)
elif decide == 1:
    w = np.array([[2,3,4],[4,3,2]])
    x = np.array([[3],[1],[2]])
    print(w @ x)