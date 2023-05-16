import numpy as np
from scipy.linalg import lu_factor, lu_solve
from itertools import islice
B1 = []
B2 = []
A = []
def matprep(arr):
    global B1,B2,A
    b = []
    A = []
    B1.clear()
    B2.clear()
    A.clear()
    b.clear()
    B1 = np.reshape(arr, (3, 4)).tolist()
    for i in B1:
        for j in range(len(i)):
            if j == 3:
                b.append(i[j])    
    A = np.delete(arr,[3,7,11])
    B2 = np.reshape(A, (3, 3)).tolist()
    return B2,b,B1
