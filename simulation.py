import constants as c
import pybullet_data
import pybullet as p
from world import WORLD
from robot import ROBOT
import time

class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.DIRECT)

        self.world = WORLD()
        self.robot = ROBOT()

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.gravity)

        self.Run()

    def __del__(self):
        p.disconnect()

    def Run(self):
        for t in range(c.STEPS):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)

            time.sleep(c.sleepInt)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

#        for s in self.robot.sensors:
#            self.robot.sensors[s].Save_Values()

#        for m in self.robot.motors:
#            self.robot.motors[m].Save_Values(self.robot)
