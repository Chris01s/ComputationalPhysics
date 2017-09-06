from numpy import zeros,array,arange,sqrt
from pylab import plot,show,axvline,figure

def f(r,t):
    x, vx, y, vy = r
    #constant
    G = 6.67e-11
    M = 1.989e30
    #calculate the first and second order derivatives
    R = sqrt(x**2 + y**2)
    fx = vx
    fxx = -G*M*x/R**3
    fy = vy
    fyy = -G*M*y/R**3
    return array([fx,fxx,fy,fyy],float)

def RichardsonExtrapolation(r,a,b,H,delta):
    X = []
    Y = []
    N = len(r)
    for t in arange(a,b,H):
        x, vx, y, vy = r
        X.append(x)
        Y.append(y)

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
            R2 = zeros([n,N],float)

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
        
    return array(X),array(Y)

#Earth
#constants
AU = 1.4710E11
Earth = 5.9722E24

#initial conditions
t = 0.0
tStop = 1*365.65*24*3600 #1 yr
H = 3600.0*24*7 #1 week
delta = 1E3/(365.65*24*3600) #km/yr
r = array([AU,0.0,0.0,3.0287E4],float)

#calculate using verlet
X,Y = RichardsonExtrapolation(r,t,tStop,H,delta)
figure(1)
plot(X,Y)

#Pluto
#initial conditions
t = 0.0
tStop = 250*365.65*24*3600 #1 yr
H = 50*3600.0*24*7 #1 week
delta = 1E3/(365.65*24*3600) #km/yr
r = array([4.4368E12,0.0,0.0,6.1218E3],float)

#calculate using verlet
X,Y = RichardsonExtrapolation(r,t,tStop,H,delta)
plot(X,Y)
show()








