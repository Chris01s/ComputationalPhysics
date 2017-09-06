from DiscreteFFTs import DFT
from pylab import plot,show,xlim
y = np.loadtxt("ExamplesAndUseful\pitch.txt",float)
c = DFT(y)
plot(abs(c))
#xlim(0,500)
show()
