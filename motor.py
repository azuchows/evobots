import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim
import numpy as np

class MOTOR:
    def __init__(self, motorName):
        self.motorName = motorName


    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robot, jointName = self.motorName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = c.maxForce)
