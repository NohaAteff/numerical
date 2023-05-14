import numpy as np
from scipy.linalg import lu_factor, lu_solve
from itertools import islice
# a = np.array([2,1,-1,1,5,2,2,-4,3,1,1,5])
c = []
b = []
k = []
def matprep(a):
    c.clear()
    k.clear()
    def slice(mat):
        # list of length in which we have to split
        length_to_split = [3,1,3,1,3,1]
        # Using islice
        matt = iter(mat)
        Output = [list(islice(matt, elem))
            for elem in length_to_split] 
        return Output
        # print(Output)
    b = slice(a) 
    
    for i in slice(a):
        if len(i) == 1:
            c.append(i)
    f=[]   
    for i in c:
        b.remove(i)
        for j in i:
            f.append(j)
            
    for i in b:
        k.append(i)
    o = np.array(k)
    f = np.array(f)
    
    def slicee(mat):
        # list of length in which we have to split
        length_to_split = [4,4,4]
        # Using islice
        matt = iter(mat)
        Output = [list(islice(matt, elem))
            for elem in length_to_split] 
        
        return Output
    return o,f,slicee(a)