import constants as c
import pybullet_data
import pybullet as p
from world import WORLD
from robot import ROBOT
import numpy as np
import time
import os

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI =  directOrGUI

        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.gravity)

        self.Run()

        np.save("tmp" + str(self.robot.ID), self.robot.feet)
        os.system("rename tmp" + str(self.robot.ID) + ".npy footprints" + str(self.robot.ID) + ".npy")

    def __del__(self):
        p.disconnect()

    def Run(self):
        for t in range(c.STEPS):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            if self.directOrGUI == "GUI":
                time.sleep(c.sleepInt)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

#        for s in self.robot.sensors:
#            self.robot.sensors[s].Save_Values()

#        for m in self.robot.motors:
#            self.robot.motors[m].Save_Values(self.robot)
