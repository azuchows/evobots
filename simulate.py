import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

STEPS = 1000

backLegAmplitude = np.pi/3
backLegFrequency = 8
backLegPhaseOffset = 0

frontLegAmplitude = np.pi/3
frontLegFrequency = 8
frontLegPhaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

robot = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robot)

backLegSensorValues = np.zeros(STEPS)
frontLegSensorValues = np.zeros(STEPS)

backLegTargetAngles = backLegAmplitude * np.sin(backLegFrequency * np.linspace(-np.pi, np.pi, STEPS) + backLegPhaseOffset)

frontLegTargetAngles = frontLegAmplitude * np.sin(frontLegFrequency * np.linspace(-np.pi, np.pi, STEPS) + frontLegPhaseOffset)

#np.save('C:/Users/zucho/Desktop/UVM/CS206/data/backLegTargetAngles', backLegTargetAngles)

#np.save('C:/Users/zucho/Desktop/UVM/CS206/data/frontLegTargetAngles', frontLegTargetAngles)

#exit()

for i in range(STEPS):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = backLegTargetAngles[i], maxForce = 30)

    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = frontLegTargetAngles[i], maxForce = 30)

    time.sleep(1/60)

p.disconnect()

np.save('C:/Users/zucho/Desktop/UVM/CS206/data/BackLegSensorData', backLegSensorValues)
np.save('C:/Users/zucho/Desktop/UVM/CS206/data/frontLegSensorData', frontLegSensorValues)
