import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, solutionID):
        self.ID = solutionID

        self.robot = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.robot)

        self.Prepare_To_Sense()

        self.Prepare_To_Act()

        self.nn = NEURAL_NETWORK("brain" + str(self.ID) + ".nndf")

        os.system("del brain" + str(solutionID) + ".nndf")

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


    def Act(self, time):
        for n in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(n):
                jointName = self.nn.Get_Motor_Neurons_Joint(n)
                desiredAngle = self.nn.Get_Value_Of(n) * c.motorJointRange
                self.motors[jointName].Set_Value(self, desiredAngle)


    def Think(self):
        self.nn.Update()
#        self.nn.Print()

    def Get_Fitness(self):
        count = 0
        sum = 0

        for sensor in ['LLFL', 'LLRL', 'LRFL', 'LRRL']:
            for t in self.sensors[sensor].values:
                sum += t
                count += 1

        average = sum / count

        transform = 10000 ** -(average+1)

        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        fitness = xPosition * transform
        file = open("tmp" + str(self.ID) + ".txt", "w")
        file.write(str(fitness))
        file.close()
        os.system("rename tmp" + str(self.ID) + ".txt fitness" + str(self.ID) + ".txt")
