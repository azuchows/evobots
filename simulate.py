import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, c.gravity)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

robot = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robot)

backLegSensorValues = np.zeros(c.STEPS)
frontLegSensorValues = np.zeros(c.STEPS)

backLegTargetAngles = c.backLegAmplitude * np.sin(c.backLegFrequency * np.linspace(-np.pi, np.pi, c.STEPS) + c.backLegPhaseOffset)

frontLegTargetAngles = c.frontLegAmplitude * np.sin(c.frontLegFrequency * np.linspace(-np.pi, np.pi, c.STEPS) + c.frontLegPhaseOffset)

#np.save('C:/Users/zucho/Desktop/UVM/CS206/data/backLegTargetAngles', backLegTargetAngles)

#np.save('C:/Users/zucho/Desktop/UVM/CS206/data/frontLegTargetAngles', frontLegTargetAngles)

#exit()

for i in range(c.STEPS):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = backLegTargetAngles[i], maxForce = c.maxForce)

    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = frontLegTargetAngles[i], maxForce = c.maxForce)

    time.sleep(c.sleepInt)

p.disconnect()

np.save('C:/Users/zucho/Desktop/UVM/CS206/data/BackLegSensorData', backLegSensorValues)
np.save('C:/Users/zucho/Desktop/UVM/CS206/data/frontLegSensorData', frontLegSensorValues)
