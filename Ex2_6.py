import math as m

def Orbital_Mech(l1, v1, M):
    '''Returns the orbital period and
    eccentricity of the orbiting body'''
    #calculations
    G = 6.67E-11
    v2 = 2*G*M/(l1*v1) - v1
    l2 = l1*v1/v2
    a = (l1 + l2)/2
    b = m.sqrt(l1*l2)

    T = 2*m.pi*a*b/(l1*v1*365.65*24*3600)
    e = (l2 - l1)/(l2 + l1)

    return T, e

M = 1.989E30 #Sun's mass

#conditions (Earth)
l1 = 1.471E11
v1 = 3.0287E4
print Orbital_Mech(l1,v1,M), "\n"

l1 = 8.7830E10
v1 = 5.4529E4
print Orbital_Mech(l1,v1,M), "\n"


