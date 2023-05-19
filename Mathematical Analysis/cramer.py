import numpy as np 
from scipy.linalg import solve
import win as pr
def cramer(n,arr):
    o,f,a=pr.matprep(arr)
    b1 = np.reshape(f,(3,1))
    a1 = np.asmatrix(o)
    A = []
    solution = []
    for i in range(n):
        top_of_x = a1.copy()
        top_of_x[:,i] = b1
        # print(top_of_x)
        A.append(top_of_x)
        det_of_top_of_x = np.linalg.det(top_of_x)
        det_of_a = np.linalg.det(a1)
        x = det_of_top_of_x / det_of_a
        solution.append(round(x))  
        # print(round(x))
    print(solution)
    for i in A:
        print(i)
    return A,solution
# A,sol = cramer(3,[2,1,-1,1,5,2,2,-4,3,1,1,5])
# print(A)
# print(sol)



