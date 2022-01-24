import numpy as np
import matplotlib.pyplot as pyplot

backLegSensorValues = np.load("C:/Users/zucho/Desktop/UVM/CS206/data/BackLegSensorData.npy")

frontLegSensorValues = np.load('C:/Users/zucho/Desktop/UVM/CS206/data/frontLegSensorData.npy')

pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 3)
pyplot.plot(frontLegSensorValues, label = "Front Leg")
pyplot.legend()
pyplot.show()
