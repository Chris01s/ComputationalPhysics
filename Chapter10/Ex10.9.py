import random
from numpy.random import randint
import numpy as np
from pylab import plot,ylabel,show,figure,legend

#populate the grid of dipoles with random spins
def populate(n):
	'''function to populate the grid of dipoles,
		and ensure that the initial value for the total
		magnetization is zero'''
		
	for i in range(N):
		for j in range(N):
			if random.random()<=0.5:
				n[i,j] = -1
			else:
				n[i,j] = 1

	while abs(np.sum(n)) > 1:
		populate(n)
	
	return n


def E_check(n):
	'''performs calculation of the total energy of the dipole lattice
		by multiplying spin states of neighbouring dipoles'''
		
	J = 1
	energy = 0
	for i in range(1,len(n)):
		s1,s2= 0,0
		for j in range(1,len(n)):
			diff = abs(i-j)
			if i==j and diff>1:
				continue
			else:
				s1 += n[i,j]*n[i,j-1]
				s2 += n[i,j]*n[i-1,j]
		energy += s1+s2
	
	return -J*energy
			

def E(n):
	'''same as above only much faster'''
	
	J = 1
	s1 = n[1:]*n[:-1]
	s2 = n[:,1:]*n[:,:-1]
	return -J*(np.sum(s1)+np.sum(s2))



if __name__ == "__main__":
	#Create a 2D array to store the quantum spin numbers
	N = 20
	s = np.ones([N,N],int)

	T = np.arange(0,3,0.5) 
	k = 1
	steps = 10000
	Mi = 0
	for temp in T:
		#set up initial conditions
		populate(s) #populate the nxn states
		E1 = E(s)
		M = []
		Etot = []
		for i in range(steps):
			#randomly choose a dipole
			i = randint(0,N)
			j = randint(0,N)
		
			#flip the spin and calculate new energy 
			s[i,j] *= -1
			E2 = E(s)
		
			#difference between two energy states
			dE = E2-E1 
		
			#decide whether to accept or reject flip
			if dE < 0:
				#accept because we want to minimise the overall energy
				#and the exp(-dE/kT) will be greater geq to 1
				E1 = E2 
				Mi = np.sum(s)
			else:
				#randomly accept or reject based on transition probability
				if random.random()<np.exp(-dE/k/temp):
					E1 = E2 #accept
					Mi = np.sum(s)
				else:
					s[i,j] *= -1 #reject

			Etot.append(E1)
			M.append(Mi)
	
		M = np.array(M)
		
		Etot = np.array(Etot)
		figure(1)
		plot(M,label="T=%f"%(temp))
		figure(2)
		plot(Etot,label="T=%f"%(temp))
	legend(loc="upper right")
show()
		
		
		
		
		
		
					
				
				
		
		
		
	
	
	
		







	
	
	
