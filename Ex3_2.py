import numpy as np
import pylab as plt


#a)
theta = np.linspace(0,2*np.pi,1000)
x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)
plt.figure(1)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#b)
theta = np.linspace(0,10*np.pi,2000)
r = theta**2
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.figure(2)
plt.plot(x,y)
plt.show()

#c)
theta = np.linspace(0,24*np.pi,2000)
r = np.exp(np.cos(theta)) - 2*np.cos(4*theta) + (np.sin(theta/12))**5
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.figure(3)
plt.plot(x,y)
plt.show()
