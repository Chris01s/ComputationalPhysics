#Ex 2.9
from __future__ import division
from visual import sphere

#Intial Conditions
M = 0 #madelung constant 
N = 50 #number of i,j,k co-ordinates in the lattice

#nested for... loops to iterate over the lattice co-ords from the origin (0,0,0)
for i in range(-N,N):
    for j in range(-N,N):
        for k in range(-N,N):
            if abs(i+j+k)%2 == 0: #calculate sign of electric potential 
                sphere(radius=0.1,pos=[i,j,k], color=color.green) #place sodium atom
            else:
                sphere(radius=0.5,pos=[i,j,k], color=color.red) #place chlorine atome
show()
