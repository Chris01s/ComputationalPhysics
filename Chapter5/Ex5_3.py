from numpy import array,sqrt,pi,exp,arange
from pylab import plot,show,legend

##perfroms Simpson Rule of integration
def Simps(f,a,b,N):
    h = abs(a-b)/N
    Simp = f(a) + f(b) 
    for k in range(1,N):
        if k%2 != 0:
            Simp += 4*f(a + k*h)
        else:
            Simp += 2*f(a + k*h)
    return Simp*h/3.0

#function
def f(t):
    return exp(-t**2)


delta = 0.1
x = arange(0,3,delta)
N = 10

Res1 = array([Simps(f,b,b+delta,N) for b in x])
print sum(Res1)
print "Fractional Error: ",(sum(Res1) - sqrt(pi)/2)/sqrt(pi)/2


#b)
#perform cumulative sum over the results vector
for i in range(1,len(x)):
    Res1[i] += Res1[i-1]
    
plot(x,Res1,label = 'Simpson\'s Rule')
legend(loc='upperright')
show()

