from random import random
from pylab import plot,show,legend
from numpy import arange
random()
#initial conditions
nPb = 0
nTl = 0
nBi209 = 0
nBi213 = 10000
Bi_213 = []
Bi_209 = []
Pb_209 = []
Tl_209 = []

#time
dt = 1.0 #time step
tmax = 20000 #total duration
tpoints = arange(0.0,tmax,dt) #time array

#constants
#half-lifes/lifetimes
p_Tl = 1 - 2**(-dt/2.2/60)
p_Bi = 1 - 2**(-dt/46/60)
p_Pb = 1 - 2**(-dt/3.3/60)

def atom_decay(natoms,p_decay):
	decay = 0
	for atom in range(natoms):
		if random()<p_decay:
			decay += 1
		else:
			continue
	return decay
	

for t in tpoints:
	Bi_213.append(nBi213)
	Bi_209.append(nBi209)
	Tl_209.append(nTl)
	Pb_209.append(nPb)
	
	Pb_decay = atom_decay(nPb,p_Pb)
	if Pb_decay > 0:
		nPb -= Pb_decay
		nBi209 += Pb_decay
		
	Tl_decay = atom_decay(nTl,p_Tl)
	if Tl_decay > 0:
		nTl -= Tl_decay
		nPb += Tl_decay
		
	#Bi213 decays
	p_Tl = 2.09/100 #probability of Bi213 -> Tl209
	for atoms in range(nBi213):
		#Decay, or not Decay?
		if random() < p_Bi:
			nBi213 -= 1
			#Decay to Tl or Pb?
			if random()<p_Tl:
				nTl += 1
			else:
				nPb += 1
		else:
			continue


plot(tpoints,Bi_213,label='Bi213')
plot(tpoints,Bi_209,label='Bi209')
plot(tpoints,Pb_209,label='Pb209')
plot(tpoints,Tl_209,label='Tl209')
legend()
show()	
	
	
	
