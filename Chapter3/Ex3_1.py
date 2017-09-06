import numpy as np
import pylab as plt

#a)

data = np.loadtxt(r'cpresources\sunspots.txt',float)
time, sunspots = np.transpose(data)
plt.figure(1)
plt.plot(time,sunspots)
plt.title('Sunspots/month since 1749')
plt.xlabel('time(Months)')
plt.ylabel('Sunspots')
plt.show()

#b)
n = 1000
plt.figure(2)
plt.plot(time[:n],sunspots[:n],'b-', label = 'Sunspots')
plt.show()

#c)
r = 5
N = len(sunspots)
a = np.array([sum(sunspots[-r+i:r+i])/(2*r) for i in range(r,N-r)])
plt.figure(2)
plt.plot(time[:1000],a[:1000],'r-',label = 'moving average')
plt.title('Sunspots/month since 1749')
plt.xlabel('time(Months)')
plt.ylabel('Sunspots')
plt.legend(loc='upperright')
plt.show()
