import numpy as np
import matplotlib.pyplot as pyplot

backLegSensorValues = np.load("C:/Users/zucho/Desktop/UVM/CS206/data/BackLegSensorData.npy")

frontLegSensorValues = np.load('C:/Users/zucho/Desktop/UVM/CS206/data/frontLegSensorData.npy')

pyplot.plot(backLegSensorValues)
pyplot.plot(frontLegSensorValues)
pyplot.show()
