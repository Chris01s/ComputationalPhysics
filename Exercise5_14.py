#Exercise 5.14

from numpy import sqrt, linspace, zeros, array
import sys
sys.path.append('C:\Users\CHRIS\Documents\Python Scripts\LearningScripts\NeumannExercises')
from gaussxw import gaussxw

def Force(z, a, b, N):
    '''first argument can be an array or single value
        that relies on at least 2 different variables'''

    def func(x,y,z):
        return (x**2 + y**2 + z**2)**(-3/2)
    
    x, w = gaussxw(N)
    xp = 0.5*((b-a)*x + (b+a))
    wp = 0.5*w*(b-a)
    y = xp
    integral = 0

    for i in range(N):
        for j in range(N):
            integral += wp[i]*wp[j]*func(xp[i],y[j], z)
    return integral

L= 10.0
m = 5.64E24
G = 6.67E-11
sigma = 10**2
z = linspace(-10,10,100)
F_z = abs(Force(z, -L/2, L/2, 100))
F_z *= G * m * sigma * z


    
    
