#Ex 2.3
from math import sqrt,pi,acos,sin,cos

x, y = input("Enter coordinates for 2D space: ")
r = sqrt(x**2 + y**2)
theta = acos(x/r)
print r, theta

x = r*cos(theta)
y = r*sin(theta)
print x, y
