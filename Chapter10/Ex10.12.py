from numpy.random import random_sample
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

#generate random points on sphere in spherical polars
n, m = random_sample(500), random_sample(500)
theta = np.arccos(1 - 2*m)
phi = 2*np.pi*n

#convert to cartesians
r = 1.0
x = r*np.sin(theta)*np.cos(phi)
y = r*np.sin(theta)*np.sin(phi)
z = r*np.cos(theta)

#3d plot
fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.scatter(x, y, z, c='r', marker='.')
plt.show()





