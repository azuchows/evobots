import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.robot = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.robot)

        self.Prepare_To_Sense()

        self.Prepare_To_Act()

        self.nn = NEURAL_NETWORK("brain.nndf")

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

            self.motors[jointName].amplitude = c.amplitude

            self.motors[jointName].frequency = c.frequency

            self.motors[jointName].offset = c.offset

            self.motors[jointName].motorValues = self.motors[jointName].amplitude * np.sin(self.motors[jointName].frequency * np.linspace(-np.pi, np.pi, c.STEPS) + self.motors[jointName].offset)

    def Act(self, time):
        for i in self.motors:
            self.motors[i].Set_Value(self, time)

    def Think(self):
        self.nn.Update()
        self.nn.Print()
