import sys
import matplotlib.pyplot as plt
import numpy

x=[10,17,18,19,25,40,80]
y = [5,6,8,10,19,25,30]

x = numpy.array(x)
y = numpy.array(y)

plt.plot(x,y)
#plt.plot(y,x)

plt.show()