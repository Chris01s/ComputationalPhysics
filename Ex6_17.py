from numpy import array,exp
from numpy.linalg import solve
import sys
sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\NumericalMethods')
from LU_Decomp import GaussElim


def f1(V1,V2):
    return V1*(1/R1 + 1/R2) - V/R1 + I0*(exp((V1-V2)/VT) - 1)

def f2(V1,V2):
    return V*(1/R1 + 1/R3) - V1*(1/R1 + 1/R2) - V2*(1/R3 + 1/R4)

def NewtonSecantMultiple(V11,V12,V21,V22,acc):
    while True:
        a = f1(V11,V21)
        b = f2(V11,V21)
        c = V12 - V11
        d = V22 - V21

        d1f1 = (f1(V12,V21) - a)/c
        d2f1 = (f1(V11,V22) - a)/d
        d1f2 = (f2(V12,V21) - b)/c
        d2f2 = (f2(V11,V22) - b)/d

        dx = array([[d1f1,d2f1],[d1f2,d2f2]],float)
        v = array([a,b],float)
        
        V11, V21 = V12,V22
        V12,V22 = array([V11,V21],float) - solve(dx,v)
        delta = array([V12-V11,V21-V22],float)
        print abs(delta)
        if min(abs(delta)) < acc:
            break
    return V12,V22

        
V = 5
R1 = 1e3
R2 = 4e3
R3 = 3e3
R4 = 2e3
I0 = 3e-9
VT = 0.05

acc = 1e-6
error = 1

V11,V12 = 1, 1.1
V21,V22 = 5, 4.9

solns = NewtonSecantMultiple(V11,V12,V21,V22,acc)
