from numpy import loadtxt,transpose,array
from pylab import plot,show


#a)
t, v = transpose(loadtxt("ExamplesAndUseful/velocities.txt",float))
#Trapezoidal method
s = 0.5*v[0] + 0.5*v[-1] + sum(v[1:-1])
print s

#b)
a = 0.5*v[0]
dist = [a]
N = len(v)
for k in range(1,N):
    dist.append(sum(v[k-1:k+1])/2 + dist[k-1])

dist = array(dist)
plot(t,dist,t,v)
show()
