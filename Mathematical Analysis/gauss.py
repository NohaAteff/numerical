import numpy as np
import sys
from itertools import islice
def slice(n,mat):
    
	# list of length in which we have to split
	length_to_split = [4,4,4]
	# Using islice
	matt = iter(np.array(mat))
	Output = [list(islice(matt, elem))
           for elem in length_to_split]
	return gauss(n,Output)
	# return gaussianElimination(Output)
 
def gauss(n,a):
    solution = []
    x = np.zeros(n)
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
            
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    print(a[0][0])
    # Back Substitution
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]

    # Displaying solution
    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]), end = '\t')
        solution.append(x[i])
    return a,solution
# print(slice(3,[2,1,-1,1,5,2,2,-4,3,1,1,5]))
