from DiscreteFFTs import DFT
from pylab import plot,show,xlim,ylim,figure
from numpy import pi,linspace,sin,array

square = []
T = linspace(0,2*pi,1000)
for t in T:
    s = 0.0
    for k in range(1,1000,2):
        s += sin(2*pi*k*t)/k
    s *= 4/pi
    square.append(s)

figure(1)
plot(T,square)

square = array(square)
c = DFT(square)
figure(2)
plot(abs(c))

sawtooth =[]
for t in T:
    s = 0.0
    for k in range(1,1000):
        s += (-1)**k * sin(2*pi*k*t)/k
    s *= 1/pi
    s = 1/2 - s
    sawtooth.append(s)

figure(3)
plot(T,sawtooth)
sawtooth = array(sawtooth)
c = DFT(sawtooth)
plot(abs(c))
show()



        
    
