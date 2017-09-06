import sys
sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\NumericalMethods')
import NumericalMethodsOfIntegration as integrate
from numpy import array

def f(x):
    return x**4 - 2*x + 1
a = 0.0
b = 2
I1, I2 = array([integrate.Trap(f,a,b,N) for N in 10,20])
err1 = abs(I1 - I2)/3.0
err2 = abs(I1 - 4.4)/4.4
err3 = abs(I2 - 4.4)/4.4

print "Compared with N = 20: ", I1,"+/-",err1
print I2,"+/-",err1
print "Compared with analytical result (4.4): ", I1,"+/-",err2
print I2,"+/-",err3

