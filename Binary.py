##This is code to produce a virtual simulation of a binary star system

from visual import *

##
##scene.lights=[]
##scene.ambient = color.black

theta = 0.0

dstar = 1.0
starpos = (0,0,0)
starrad = 0.1
starcol = color.black

starlight = local_light(pos=starpos,
                   color=starcol)
star = sphere(pos = starpos, radius = starrad, color=starcol)
star.mass = 4

giant = sphere(material=materials.emissive)
giant.pos = vector(-1,1,0)
giant.radius = 0.075
giant.color = color.red
giant.mass = 2.5
giant.p = vector(0.2, 0.2, -0.3) * giant.mass

dwarf = sphere(material=materials.emissive)
dwarf.pos = vector(1,0,0)
dwarf.radius = giant.radius
dwarf.color = color.yellow
dwarf.mass = 1
dwarf.p = -giant.p

for a in [giant, dwarf]:
  a.orbit = curve(color=a.color, radius = 0.01)

dt = 0.02
G = 1 
while 1:
  rate(100)

  dist = dwarf.pos - giant.pos
  force = G * star.mass * dwarf.mass * dist / mag(dist)**3
  
  ## leapfrog method
  giant.p = giant.p + force*dt
  dwarf.p = dwarf.p - force*dt

  for a in [giant, dwarf]:
    a.pos = a.pos + a.p/star.mass * dt
    #a.orbit.append(pos=a.pos)
