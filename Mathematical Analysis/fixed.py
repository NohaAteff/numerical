import numpy
import math


# Implementing Fixed Point Iteration Method

def fixedPointIteration(i,j,x0, e):
    
    def f(x):
        return eval(i, {'x': x, 'np': numpy,'sqrt':math.sqrt})

    def g(x):
        return eval(j, {'x': x, 'np': numpy,'sqrt':math.sqrt})
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 0
    flag = 1
    # N = int(N)
    xold = float(0)
    x0 = float(x0)
    x1 = float(0)
    e = float(e)
    iterations = []
    condition = True
    while condition:
        x1 = g(x0)
        # print('Iteration-%d, x1 = %0.6f , f(x1) = %0.6f %' % (step, x1, f(x1)))
        iterations.append('Iteration-%d, x1 = %0.6f , f(x1) = %0.6f, E=%0.2f' % (step, x1, f(x1),abs((x1-xold)/x1)*100))
        x0 = float(x1)
        step = step + 1
        condition = abs((x1-xold)/x1)*100 > e
        xold=x1
    print('\nRequired root is: %0.8f' % x1)
    print(len(iterations))
    return iterations,x1

def fixedPointIteration(i,j,x0, N):
    print('entered')
    def f(x):
        return eval(i, {'x': x, 'np': numpy,'sqrt':math.sqrt})

    def g(x):
        return eval(j, {'x': x, 'np': numpy,'sqrt':math.sqrt})
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 0
    flag = 1
    N = int(N)
    xold = float(0)
    x0 = float(x0)
    x1 = float(0)
    # e = float(e)
    iterations = []
    condition = True
    while condition:
        x1 = g(x0)
        # print('Iteration-%d, x1 = %0.6f , f(x1) = %0.6f %' % (step, x1, f(x1)))
        iterations.append('Iteration-%d, x1 = %0.6f , f(x1) = %0.6f, E=%0.2f' % (step, x1, f(x1),abs((x1-xold)/x1)*100))
        x0 = float(x1)
        step = step + 1
        if step > N:
            flag = 0
            break
        condition = step<N
        xold=x1
    print('\nRequired root is: %0.8f' % x1)
    print(len(iterations))
    return iterations,x1
