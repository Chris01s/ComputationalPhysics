from numpy import loadtxt
from pylab import imshow, gray,show

stmData = loadtxt(r'ExamplesAndUseful/stm.txt',float)
gray()
imshow(stmData, vmax=abs(stmData).max()*1.3)
show()
