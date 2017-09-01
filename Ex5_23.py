from numpy import loadtxt,zeros,sqrt,pi,cos,sin,shape
from pylab import imshow,show,gray

w = loadtxt('ExamplesAndUseful/stm.txt',float)
earth = loadtxt('ExamplesAndUseful/altitude.txt',float)

def partialDiff(data,h):
    nx,ny = shape(data)
    I =  zeros((nx,ny))
    theta = pi/4
    ax,ay,az = (cos(theta),sin(theta),0)
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            dx = (data[i+1,j] - data[i-1,j])/2/h
            dy = (data[i,j+1] - data[i,j-1])/2/h
            I[i,j] = (ax*dx + ay*dy  - az)/sqrt(dx**2 + dy**2 + 1)
    return I


I = partialDiff(w,2.5)
imshow(I)
show()
I = partialDiff(earth,30000)
imshow(I,vmax=0.03,vmin=-0.01)
show()
