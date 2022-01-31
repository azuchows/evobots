import constants as c
import pybullet_data
import pybullet as p
from world import WORLD
from robot import ROBOT
import time

class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)

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
#           self.robot.Sense(self, t)
            #pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = backLegTargetAngles[i], maxForce = c.maxForce)

            #pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = frontLegTargetAngles[i], maxForce = c.maxForce)

            time.sleep(c.sleepInt)

        for s in self.robot.sensors:
            print(self.robot.sensors[s].values)
