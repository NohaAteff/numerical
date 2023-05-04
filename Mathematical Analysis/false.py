# Defining Function
import numpy
import math
# i = input("fn: ")


# Implementing False Position Method
def falsePosition(i,x0,x1,e):
    iterations = []
    x0 = float(x0)
    x1 = float(x1)
    x2 = float(0)
    # x2old = float(x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) ))
    e = float(e)
    def f(x):
        return eval(i, {'x': x, 'np': numpy.log, 'cos':math.cos,'sin':math.sin,'exp':math.exp})
    #initialize xrold to be used in the condition before assigning xr's value to it
    x2old =0 

    if f(x0) * f(x1) < 0.0:
        step = 1
        print('\n\n** FALSE POSITION METHOD IMPLEMENTATION **')
        condition = True
        while condition:
            x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
            print('I-%d,xl=%0.6f,xu=%0.6f ,x2 = %0.6f and f(x2) = %0.6f,|%0.6f' % (step, x0, x1, x2, f(x2),abs((x2-x2old)/x2)*100))
            iterations.append('i-%d, xl=%0.3f, f(xl)=%0.3f, xu=%0.3f, f(xu)=%0.3f, x2 = %0.3f and f(x2) = %0.3f,|%0.2f' % (step, x0, f(x0), x1, f(x1), x2, f(x2),abs((x2-x2old)/x2)*100))
            if f(x0) * f(x2) < 0:
                x1 = x2
            else:
                x0 = x2
            step = step + 1
            condition = abs((x2-x2old)/x2)*100 > e
            x2old = x2
            
        print('\nRequired root is: %0.8f' % x2)
    else:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    
    return iterations , x2
