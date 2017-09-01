from numpy import zeros,array,arange,sin,pi,reshape
from pylab import plot,show,axvline


def f(r,t):
    '''This function returns a vector of the simultaneous
    multivariable equations the arguments are a vector, r,
    and t the independent variable'''
    #parse the vector 
    theta,omega = r
    #set up intial conditions
    g = 9.81
    l = 0.1
    #calculate values from respective functions
    ftheta = omega
    fomega = -g*sin(theta)/l
    #return the results as a vector 
    return array([ftheta,fomega],float)

def RichardsonExtrapolation(r,a,b,H,delta):

    THETA = []

    for t in arange(a,b,H):
        theta, omega = r
        THETA.append(theta)

        ##initiate with Modified midpoint with only one step, size H
        n = 1
        r1 = r + 0.5*H*f(r,t)
        r2 = r + H*f(r1,t + 0.5*H)
        #calculate first solution estimate in first row, R1
        R1 = array([0.5*(r2 + r1 + 0.5*H*f(r2,t + H))])

        #estimate intial error
        error = 2*H*delta

        #Now perform modified midpoint for greater number of steps
        #then use Richardson extrapolation
        while error > H*delta:
            #increase number of steps and split interval H up accordingly
            n += 1
            h = H/n
            R2 = zeros([n,2],float)

            #Use modified midpoint method n times
            r1 = r + 0.5*h*f(r,t)
            r2 = r + h*f(r1,t + 0.5*h)
            for i in range(1,n):
                r1 += h*f(r2,t + i*h)
                r2 += h*f(r1,t + (i + 1/2)*h)

            #calculate the first solution estimate in the new row,R2
            R2[0] = 0.5*(r2 + r1 + 0.5*h*f(r2,t+H))

            #Extrapolate
            for m in range(n-1):
                epsilon = (R2[m] - R1[m])/((float(n)/(n-1))**(2*(m+1)) - 1)
                R2[m+1] = R2[m] + epsilon

            #equate previous row to new row and new error from extrapolation
            R1 = R2.copy()
            error = abs(epsilon[0])

        #once the target accuracy has been acheived, take last value as solution
        r = R2[-1]
        
    return array(THETA)

delta = 1e-8
a = 0.0
b = 10.0
N = 100
H = abs(a-b)/N
r = array([179*pi/180,0.0],float)

time = arange(a,b,H)
theta = RichardsonExtrapolation(r,a,b,H,delta)
plot(time,theta)
for i in range(len(time)):
    try:
        axvline(time[i*5],ls='dotted')
    except IndexError:
        break
    
show()



    
    
    
    
    
    
    
    



