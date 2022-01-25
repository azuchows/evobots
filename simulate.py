import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

STEPS = 1000

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

robot = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robot)

backLegSensorValues = np.zeros(STEPS)
frontLegSensorValues = np.zeros(STEPS)

targetAngles = np.pi/4 * np.sin(np.linspace(-np.pi, np.pi, STEPS))

#np.save('C:/Users/zucho/Desktop/UVM/CS206/data/targetAngles', targetAngles)

for i in range(STEPS):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles[i], maxForce = 30)

    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles[i], maxForce = 30)

    time.sleep(1/60)

p.disconnect()

np.save('C:/Users/zucho/Desktop/UVM/CS206/data/BackLegSensorData', backLegSensorValues)
np.save('C:/Users/zucho/Desktop/UVM/CS206/data/frontLegSensorData', frontLegSensorValues)
