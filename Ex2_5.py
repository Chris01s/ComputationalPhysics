import math as m

#Constants
eV = 1.6E-19
E = 10*eV #Particle energy
V = 9*eV #barrier height
mass = 9.11E-31 # particle's mass
hbar = 6.64E-34/(2*m.pi)

#wavevectors
k1 = m.sqrt(2*mass*E)/hbar
k2 = m.sqrt(2*mass*(E-V))/hbar
#Prbabilities
T = 4*k1*k2/sum([k1,k2])**2
R = ((k1-k2)/sum([k1,k2]))**2

print "T = ", T, "R = ", R


