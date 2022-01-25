import numpy as np
import matplotlib.pyplot as plt

#backLegSensorValues = np.load("C:/Users/zucho/Desktop/UVM/CS206/data/BackLegSensorData.npy")

#frontLegSensorValues = np.load('C:/Users/zucho/Desktop/UVM/CS206/data/frontLegSensorData.npy')

#plt.plot(backLegSensorValues, label = "Back Leg", linewidth = 3)
#plt.plot(frontLegSensorValues, label = "Front Leg")
#plt.legend()

targetAngles = np.load('C:/Users/zucho/Desktop/UVM/CS206/data/targetAngles.npy')
plt.plot(targetAngles)
plt.show()
