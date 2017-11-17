import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy


irange = 0.1
rng = numpy.random.RandomState([2015, 10, 10])
numpyWeights = rng.uniform(
            -irange, irange,
            (784, 100))

print(numpyWeights.shape)
imshowArray = rng.uniform(
            -irange, irange,
            (280, 280))

for counter in range(0,10):
     intermediateWeights = numpyWeights.T[counter*10:(counter+1)*10,:]
     print(intermediateWeights.shape)
     reshapedIntermediateWeights = intermediateWeights.reshape(280,28)
     imshowArray[:,counter*28:(counter+1)*28] = reshapedIntermediateWeights

plt.imshow(imshowArray)
plt.show()
