import pybullet_data
import pybullet as p
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

robotId = p.loadURDF("body.urdf")

for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)

p.disconnect()
