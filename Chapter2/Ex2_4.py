#Ex 2.4

from math import sqrt

x,v = input("Enter distance travelled(lyrs), and the speed of craft \
(fraction of c): ")

gamma = 1/sqrt(1 - v**2)

#a) simple time-distance relationship: note the time will appear dilated
#on the craft from this frame of reference
time = x/v

#b) time will tick as normal on the craft, but the distance to planet x will
# have appeared to contract by a factor of gamma
x_contracted = x/gamma
time = x_contracted/v
print x_contracted,time



