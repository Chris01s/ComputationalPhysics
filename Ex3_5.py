from __future__ import division, print_function
from visual import *
from cmath import exp
from math import pi
#from numpy import empty

scene.lights=[]
scene.ambient = color.black
sphere(pos=(0,0,0),radius=40,color=(1,1,1), material=materials.emissive)

c1 = 2e-3
c2 = 0.5

class planet:	
	
	def __init__(self,r_radius,r_orbit,period):
	#self = sphere()
		
		self.sphere = sphere()
		print("Object {} created".format([r_radius,r_orbit,period]))
		
		self.T = period
		self.r_orbit = r_orbit #108.2e6/100
		self.sphere.radius = r_radius #6052
		self.move(0)		
				
	def move(self,t):
		
		omega = 2*pi/self.T
		theta = omega*t
		
		pos = self.r_orbit*exp(1j*theta)
		self.sphere.pos = [pos.real,pos.imag,0]


table = [
	[2440,	57.9,		88,	color.red],
	[6052,	108.2,	224.7, color.magenta],
	[6371,	149.6	,	365.3, color.blue],
	[3386,	227.9,	687.0, color.orange],
	[69173,	778.5,	4331.6,color.red],
	[57316,	1433.4,	10759.2,color.yellow]]

planets = []
for r_radius,r_orbit,period,color in table:
	s = planet(r_radius*c1,r_orbit,period/c2)
	s.sphere.color = color
	planets.append(s)

t = 0
while True:
	rate(100)
	for i in planets:
		i.move(t*c2)
	t+=1
