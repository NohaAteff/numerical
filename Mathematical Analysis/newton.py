from scipy.misc import derivative
import numpy
import math

def newtonRaphson(i,x0,e,N):
    iterations = []
    x0 = float(x0)
    x0ld = float(x0)
    e = float(e)
    N = int(N)
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
        
        #This should be printed in the GUi
        print('Iteration-%d, xi = %0.6f and f(xi) = %0.6f' % (step, xk, f(xk)))
        iterations.append('Iteration-%d, xi = %0.6f , f(xi) = %0.6f,g(xi)=%0.3f,E=%0.2f' % (step, xk, f(xk),g(xk),abs((x0-x0ld)/x0)*100))
        
        x0 = xk
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs((x0-x0ld)/x0)*100 > e
        x0ld=x0
    
    if flag==1:
        print('\nRequired root is: %0.8f' % xk)
    else:
        print('\nNot Convergent.')
    return iterations , xk

# Input Section
# x0 = input('Enter Guess: ')
# e = input('Tolerable Error: ')
# N = input('Maximum Step: ')

# Converting x0 and e to float
# x0 = float(x0)
# e = float(e)

# # Converting N to integer
# N = int(N)


#Note: You can combine above three section like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
# newtonRaphson(x0,e,N)