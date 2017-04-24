def f(x):
	import math
	return 60*math.e**(math.log(0.5)/55.6 * x)

def radiationExposure(start, stop, step):
    
    n = start
    y = stop
    finalValue = 0
    
    while n < y :
        
        if y == n:
            print y

        elif n <= y:
            finalValue += step*f(n)
    
        n += step
        
    print finalValue 

radiationExposure(600, 1200, 5)