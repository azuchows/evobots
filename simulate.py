import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import math

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

robot = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robot)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = (-math.pi / 4), maxForce = 500)

    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = (math.pi / 4), maxForce = 500)

    time.sleep(1/60)

p.disconnect()

np.save('C:/Users/zucho/Desktop/UVM/CS206/data/BackLegSensorData', backLegSensorValues)
np.save('C:/Users/zucho/Desktop/UVM/CS206/data/frontLegSensorData', frontLegSensorValues)
