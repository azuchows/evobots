import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR

class ROBOT:
    def __init__(self):
        self.robot = p.loadURDF("body.urdf")
        self.motors = {}

        pyrosim.Prepare_To_Simulate(self.robot)

        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, time):
        for i in self.sensors:
            self.sensors[i].Get_Value(time)
