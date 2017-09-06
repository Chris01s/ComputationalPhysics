from pylab import plot,show,legend,figure,axvline
from numpy import arange,array,sin,pi


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

def Adaptiverk4(f,t,r,tStop,h,sig=1e-6):
    '''The function performs the RK4 method but with a varying stepsize
       as it is generally unknown what step size one should take:
           f = user defined function of interest
           t = starting value of time
           r = array of starting values for the variables of interest
           tStop = end value of time
           h = initial value time step
           sig = target precision of the runge kutta calc. per unit time
        The function return two arrays; T = time array, X = variable of interest'''

    def rk4(h,x,t):
        k1 = h*f(x,t)
        k2 = h*f(x + k1*0.5, t + h*0.5)
        k3 = h*f(x + k2*0.5, t + h*0.5)
        k4 = h*f(x + k3, t + h) 
        return (k1 + 2*(k2 + k3) + k4)/6.0
        
    def adaptiveStep(h,r,t,sig):
        r1 = r + rk4(h,r,t) 
        r1 += rk4(h,r1,t+h) 
        r2 = r + rk4(2*h,r,t)
        x1,v1 = r1
        x2,v2 = r2
    
        Eacc = abs(x1-x2)/30.0
        Etarget = h*sig
        rho = Etarget/Eacc
        hprime = h*rho**(1/4.0)
    
        if rho > 1.0:
            return hprime,r1
        else:
            if(abs(hprime) > 2*abs(h)): hprime = 2*h
            elif (abs(hprime) < 0.1*abs(h)): hprime = 0.1*h
            return adaptiveStep(hprime,r,t,sig)


    X = []
    T = []
    while(t < tStop):
        x,v = r
        X.append(x)
        T.append(t)
        h,r = adaptiveStep(h,r,t,sig)
        t += h
    return array(T),array(X)

t,tStop = 0.0,5.0
h = 0.1
x = array([179*pi/180,0.0],float)
T,X = Adaptiverk4(f,t,x,tStop,h)
for t in T[::10]:
    axvline(x=t, color='k',ls='dashed') 
plot(T,X,'-')
show()



