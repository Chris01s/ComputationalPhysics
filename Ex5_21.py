#Ex 5.21
from numpy import meshgrid, pi, linspace, hypot, array, sort, zeros,sqrt,log
import matplotlib.pyplot as plt

#a)
# Dipole charge (C), Permittivity of free space (F.m-1)
eps0 = 1e-7
k = 1/(4*pi*eps0)

# Cartesian axis system with origin at the dipole (m)
X = linspace(-1.0, 1.0, 100)
Y = X.copy()
X, Y = meshgrid(X, Y)

# Dipole electrostatic potential (V), using point dipole approximation
Phi = k*X/hypot(X, Y)**3

plt.imshow(Phi)
fig = plt.figure()
ax = fig.add_subplot(111)
#Draw contours at values of Phi given by levels
levels = array([10**pw for pw in linspace(0,7,20)])
levels = sort(list(-levels) + list(levels))
#Monochrome plot of potential
ax.contour(X, Y, Phi, levels = levels, colors='b', linewidth=2)
plt.show()

n = len(Phi)
E_x = zeros((n,n))
E_y = zeros((n,n))
h = 0.01
for i in range(1,n-1):
    for j in range(1,n-1):
        E_x[i,j] = (Phi[i+1,j] - Phi[i-1,j])/2/h
        E_y[i,j] = (Phi[i,j+1] - Phi[i,j-1])/2/h
        
E = sqrt(E_x**2 + E_y**2)
plt.imshow(E, vmax=1e8, vmin=-1e8)

fig = plt.figure()
ax = fig.add_subplot(111)
# Plot the streamlines with an appropriate colormap and arrow style
color = log(E)
ax.streamplot(X, Y, E_x, E_y, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_aspect('equal')
plt.show()

