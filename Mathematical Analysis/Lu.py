import numpy as np
from scipy.linalg import lu_factor, lu_solve,lu
import win as prep
def luu(a):
    A,b,s = prep.matprep(a)
    # A = np.array([[2, 5, 8], [5, 2, 2], [7, 5, 6]])
    # b = np.array([7, 8, 6])
    lul, piv = lu_factor(A)
    x = lu_solve((lul, piv), b)
    print(x)
    
    
    p, l, u = lu(s)
    
    return lul,x,l
