from visual import *

atoms=[]
for i in range(-2,3):
    s = sphere(pos=(i,0,0),radius = 0.1)
    atoms.append(s)

while True:
    rate(30)
    for atom in atoms:
        atom.pos += 0.001
    
