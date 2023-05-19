import numpy
# Defining Function
# i = input("fn: ")



# Implementing Secant Method
def secant(i,x0,x1,e):
    iterations = []
    x0 = float(x0)
    x0ld = float(x0)
    x1 = float(x1)
    e = float(e)
    # N = int(N)
    def f(x):
        return eval(i, {'x': x, 'np': numpy})
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 0
    condition = True
    x0ld = x1
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        xs = x1 - (x0-x1)*f(x1)/( f(x0) - f(x1) ) 
        if step==0:
            print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f,|e: -' % (step, xs, f(xs)))
            iterations.append('i-%d,xi-1=%0.3f,f(xi-1)=%0.3f,xi=%0.3f,f(i)=%0.3f,x2 = %0.3f and f(x2) = %0.3f,|e:-' % (step,x0,f(x0),x1,f(x1), xs, f(xs)))
        else:
            print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f,|e: %0.6f' % (step, xs, f(xs),abs((xs-x0ld)/xs)*100))
            iterations.append('i-%d,xi-1=%0.3f,f(xi-1)=%0.3f,xi=%0.3f,f(i)=%0.3f,x2 = %0.3f and f(x2) = %0.3f,|e: %0.3f' % (step,x0,f(x0),x1,f(x1), xs, f(xs),abs((xs-x0ld)/xs)*100))

        # print(x0ld,", ",xs,", ",abs((xs-x0ld)/xs)*100)
        x0 = x1
        x1 = xs
        step = step + 1
        # if step > N:
        #     print('Not Convergent!')
        #     break
        
        condition = abs((xs-x0ld)/xs)*100 > e
        x0ld = xs
        
    print('\n Required root is: %0.8f' % xs)
    return iterations,xs

def secant(i,x0,x1,N):
    iterations = []
    x0 = float(x0)
    x0ld = float(x0)
    x1 = float(x1)
    # e = float(e)
    N = int(N)
    def f(x):
        return eval(i, {'x': x, 'np': numpy})
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    x0ld = x1
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        xs = x1 - (x0-x1)*f(x1)/( f(x0) - f(x1) ) 
        
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f,|e: %0.6f' % (step, xs, f(xs),abs((xs-x0ld)/xs)*100))
        iterations.append('i-%d,xi-1=%0.3f,f(xi-1)=%0.3f,xi=%0.3f,f(i)=%0.3f,x2 = %0.3f and f(x2) = %0.3f,|e: %0.3f' % (step,x0,f(x0),x1,f(x1), xs, f(xs),abs((xs-x0ld)/xs)*100))
        print(x0ld,", ",xs,", ",abs((xs-x0ld)/xs)*100)
        x0 = x1
        x1 = xs
        step = step + 1
        # if step > N:
        #     print('Not Convergent!')
        #     break
        
        condition = step<N
        x0ld = xs
        
    print('\n Required root is: %0.8f' % xs)
    return iterations,xs
