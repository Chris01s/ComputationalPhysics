from visual import *
import random as r
import math
from numpy import array


scene.lights=[]
scene.ambient = color.black

theta = 0.0

dstar = 1.0
starpos = (0,0,0)
starrad = 0.7
starcol = (1.0,1.0,1.0)

starlight = local_light(pos=starpos,
                   color=starcol)
star = sphere(pos = starpos, radius = starrad, color=starcol,
                    material=materials.emissive)

class planet:	
	
	def __init__(self,r_radius,r_orbit,period):
	#self = sphere()
		
		self.sphere = sphere(make_trail=true)
		print("Object {} created".format([r_radius,r_orbit,period]))
		
		self.T = period
		self.r_orbit = r_orbit #108.2e6/100
		self.sphere.radius = r_radius #6052
		self.move(0)		
				
	def move(self,t):
		
		omega = 2*pi/self.T
		theta = omega*t
		
		pos = self.r_orbit*exp(1j*theta)
		self.sphere.pos = [pos.real,0,pos.imag]


    
BODIES = array([[ 0.00350827,  0.04039347,  0.00817905],
       [ 0.00870165,  0.07548486,  0.02088445],
       [ 0.00916032,  0.10436724,  0.03395234],
       [ 0.00486844,  0.1589926 ,  0.06385233],
       [ 0.09945794,  0.54311427,  0.40259499],
       [ 0.08240978,  1.        ,  1.        ]])*30
BODIES[:,0] /= 5
planets = []
for r_radius,r_orbit,period in BODIES:
	s = planet(r_radius,r_orbit,period)
	s.sphere.color = (r.randint(0,2)*0.5,r.randint(0,2)*0.5,r.randint(0,2)*0.5)
	planets.append(s)

dt = 0.01
t = 0
while True:
    rate(30)
    star.pos = starpos
    starlight.pos = starpos
    for i in planets:
        i.move(t*0.001)
    t+=1

