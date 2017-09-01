#Ex 2.9
import math as m

#Intial Conditions
M = 0 #madelung constant 
N = 50 #number of i,j,k co-ordinates in the lattice

#nested for... loops to iterate over the lattice co-ords from the origin (0,0,0)
for i in range(-N,N):
    for j in range(-N,N):
        for k in range(-N,N):
            #exclude particle at the origin (0,0,0)
            if (i,j,k) == (0,0,0):
                continue
            else:
                if abs(i+j+k)%2 == 0: #calculate sign of electric potential 
                    sign = 1 #due to sodium atom
                else:
                    sign = -1 #due to chlorine atome
                M += sign/m.sqrt(i**2 + j**2 + k**2) #madelung const.
print M
