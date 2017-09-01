from pylab import plot,show,legend,figure
from numpy import array,copy,sqrt,pi,log,transpose

AU = 1.4989E11
YR = 3600*24*365.0

def f(r,t):
    #parse the function vector
    x,vx,y,vy = r
    #intial conditions
    M = 1.989E30
    G = 6.67E-11
    #calculate the derivatives
    fx = vx
    fy = vy
    R = sqrt(x**2 + y**2)
    fxx = -G*M*x/R**3
    fyy = -G*M*y/R**3
    return array([fx,fxx,fy,fyy],float)

def Adaptiverk4(f,t,r,tStop,h,sig=1e3/YR):
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
        x1,vx1,y1,vy1 = r1
        x2,vx2,y2,vy2 = r2
    
        EaccX = abs(x1-x2)/30.0
        EaccY = abs(y1-y2)/30.0
        Eacc = sqrt(EaccX**2 + EaccY**2)
        Etarget = h*sig
        rho = Etarget/Eacc
        hprime = h*rho**(1/4.0)
    
        if rho > 1.0:
            return hprime,r1
        else:
            if(abs(hprime) > 2*abs(h)): hprime = 2*h
            elif (abs(hprime) < 0.1*abs(h)): hprime = 0.1*h
            return adaptiveStep(hprime,r,t,sig)

    R = []
    while(t < tStop):
        R.append(r)
        h,r = adaptiveStep(h,r,t,sig)
        t += h
    return array(R)


r = array([4E12,0.0,0.0,500.0],float)
h = 1.0*YR
t = 0.0
tStop = 30*YR
soln = Adaptiverk4(f,t,r,tStop,h)
x,vx,y,vy = transpose(soln)
plot((x/AU)[::10],(y/AU)[::10],'o')
show()
