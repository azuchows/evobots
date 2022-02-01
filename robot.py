import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c

class ROBOT:
    def __init__(self):
        self.robot = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.robot)

        self.Prepare_To_Sense()

        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, time):
        for i in self.sensors:
            self.sensors[i].Get_Value(time)

    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.offset

        self.motorValues = self.amplitude * np.sin(self.frequency * np.linspace(-np.pi, np.pi, c.STEPS) + c.offset)

    def Act(self, time):
        for i in self.motors:
            self.motors[i].Set_Value(self, time)
