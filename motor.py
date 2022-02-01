import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim
import numpy as np

class MOTOR:
    def __init__(self, motorName):
        self.motorName = motorName

    def Set_Value(self, robot, time):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robot, jointName = self.motorName, controlMode = p.POSITION_CONTROL, targetPosition = robot.motorValues[time], maxForce = c.maxForce)

    def Save_Values(self, robot):
        np.save('C:/Users/zucho/Desktop/UVM/CS206/data/motorValues', robot.motorValues)
