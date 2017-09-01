#Ex 2.2
from math import sqrt,pi

G = 6.67E-11
R_E = 6371E3 #metres
M_E = 5.97E24 #kilogramms
time = float(input("enter time for orbital period: "))#seconds
height = pow(G*M_E*time*time/(4.0*pi**2),1/3.0) - R_E

print height
