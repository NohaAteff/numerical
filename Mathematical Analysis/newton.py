from scipy.misc import derivative
import numpy
import math

def newtonRaphson(i,x0,e):
    iterations = []
    x0 = float(x0)
    x0ld = float(x0)
    e = float(e)
    # N = int(N)
    x0ld = x0
    def f(x):
        return eval(i, {'x': x, 'np': numpy,'sin':math.sin,'cos':math.cos,'sqrt':math.sqrt,'e':math.exp})

    # Defining derivative of function
    def g(x):
        
        return derivative(f,x)

    # Implementing Newton Raphson Method

    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        xk = x0 - f(x0)/g(x0)
        
        if step==0:
            print('Iteration-%d, xi = %0.6f and f(xi) = %0.6f' % (step, xk, f(xk)))
            iterations.append('Iteration-%d, xi = %0.6f , f(xi) = %0.6f,g(xi)=%0.3f,E=-' % (step, xk, f(xk),g(xk)))
        else:
            print('Iteration-%d, xi = %0.6f and f(xi) = %0.6f' % (step, xk, f(xk)))
            iterations.append('Iteration-%d, xi = %0.6f , f(xi) = %0.6f,g(xi)=%0.3f,E=%0.2f' % (step, xk, f(xk),g(xk),abs((x0-x0ld)/x0)*100))

        # print('Iteration-%d, xi = %0.6f and f(xi) = %0.6f' % (step, xk, f(xk)))
        # iterations.append('Iteration-%d, xi = %0.6f , f(xi) = %0.6f,g(xi)=%0.3f,E=%0.2f' % (step, xk, f(xk),g(xk),abs((x0-x0ld)/x0)*100))
        
        x0 = xk
        step = step + 1
        
        # if step > N:
        #     flag = 0
        #     break
        
        condition = abs((x0-x0ld)/x0)*100 > e
        x0ld=x0
    
    if flag==1:
        print('\nRequired root is: %0.8f' % xk)
    else:
        print('\nNot Convergent.')
    return iterations , xk

def newtonRaphson(i,x0,N):
    iterations = []
    x0 = float(x0)
    x0ld = float(x0)
    # e = float(e)
    N = int(N)
    x0ld = x0
    def f(x):
        return eval(i, {'x': x, 'np': numpy,'sin':math.sin,'cos':math.cos,'sqrt':math.sqrt,'e':math.exp})

    # Defining derivative of function
    def g(x):
        
        return derivative(f,x)

    # Implementing Newton Raphson Method

    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 0
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        xk = x0 - f(x0)/g(x0)
        
        
        if step==0:
            print('Iteration-%d, xi = %0.6f and f(xi) = %0.6f' % (step, xk, f(xk)))
            iterations.append('Iteration-%d, xi = %0.6f , f(xi) = %0.6f,g(xi)=%0.3f,E=-' % (step, xk, f(xk),g(xk)))
        else:
            print('Iteration-%d, xi = %0.6f and f(xi) = %0.6f' % (step, xk, f(xk)))
            iterations.append('Iteration-%d, xi = %0.6f , f(xi) = %0.6f,g(xi)=%0.3f,E=%0.2f' % (step, xk, f(xk),g(xk),abs((x0-x0ld)/x0)*100))

        x0 = xk
        step = step + 1
        
        # if step > N:
        #     flag = 0
        #     break
        
        condition = step<N
        x0ld=x0
    
    if flag==1:
        print('\nRequired root is: %0.8f' % xk)
    else:
        print('\nNot Convergent.')
    return iterations , xk

