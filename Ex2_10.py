import math as m
import pylab as plt
from numpy import array,where

def OddEvenZero(A,Z):
    if A%2 == 0:
        if Z%2 == 0:
            a5 = 12.0
        else:
            a5 = -12.0
    else:
        a5 = 0.0
    return a5

def BindingEnergy(A,Z):
    #Binding energy
    a1 = 15.67
    a2 = 17.23
    a3 = 0.75
    a4 = 93.2
    a5 = OddEvenZero(A,Z)
    B = (a1*A) - (a2*A**(2/3.0)) - (Z**2 * a3/A**(1/3.0)) -\
        (a4/A * (A-2*Z)**2) + (a5/m.sqrt(A))
    return B

##a)
#Nuclear conditions
A = 58
Z = 28
B = BindingEnergy(A,Z)
print B

##b)
#Binding Energy per nucleon
print B/A


##c)
#Produce array of Binding energy per nucleon for each value of A in range Z to 3Z
B_A = array([BindingEnergy(A,Z)/A for A in range(Z,3*Z)])
A = range(Z,3*Z)
#print results
print "Max BE/Nuc ", max(B_A), " occurs at A = ", A[where(B_A == max(B_A))[0][0]]
#plot of BE/Nucleon curve for Nickel (Z=28)
plt.plot(A,B_A, A[where(B_A == max(B_A))[0][0]],max(B_A),'o')
plt.show()

#d)
#Most interesting part of the exercise
#create empty lists for max BE and corresponding atomic mass A
maxBE = []
A_n = []
#iterate nuclear mass from Z:1 to 100
for Z in range(1,101):
    #Calculate BE/Nucleon as before in part c) and append result to list
    B_A = array([BindingEnergy(A,Z)/A for A in range(Z,3*Z)])
    maxBE.append(max(B_A))
    A = range(Z,3*Z)
    #obtain atomic mass where maxBE occurs and append the result to list
    A_n.append(A[where(B_A == max(B_A))[0][0]])

#plot looks like the familiar Binding Energy per nucleon curve
plt.plot(A_n,maxBE,'-')
plt.show()
#maximum BE is occuring at A = 50, unfortunately not in agreement with Iron 56
print "Max BE/Nuc ", max(maxBE), " occurs at A = ", A_n[where(maxBE == max(maxBE))[0][0]]


    
    
    
