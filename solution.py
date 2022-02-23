import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, ID):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = ID
        self.age = 1


    def Start_Simulation(self, directOrGUI):
        self.Generate_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID) + " &")


    def Final_Simulation(self):
        self.Generate_Brain()
        os.system("python simulate.py GUI " + str(self.myID))


    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

        file = open("fitness" + str(self.myID) + ".txt", "r")

        self.fitness = file.read()
#        print(self.fitness)
        file.close()
#        print("fitness: " + str(self.fitness))
        os.system("del fitness" + str(self.myID) + ".txt")


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.End()


    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name = "Torso", pos = [0,0,1] , size = [1.5,0.5,0.25])

        # Right Front Leg
        pyrosim.Send_Joint(name = "Torso_URFL", parent = "Torso", child = "URFL", type = "revolute", position = [0.5, 0.25, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "URFL", pos = [0, 0.0625, -0.375], size = [0.125, 0.125, 0.75])
        pyrosim.Send_Joint(name = "URFL_LRFL", parent = "URFL", child = "LRFL", type = "revolute", position = [0, 0.0625, -0.675], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LRFL", pos = [0.25, 0, 0], size = [0.5, 0.125, 0.125])
        pyrosim.Send_Joint(name = "LRFL_RFF", parent = "LRFL", child = "RFF", type = "revolute", position = [0.4375, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "RFF", pos = [0, 0, -0.125], size = [0.125, 0.125, 0.25])

        # Left Rear Leg
        pyrosim.Send_Joint(name = "Torso_ULRL", parent = "Torso", child = "ULRL", type = "revolute", position = [-0.5, -0.25, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "ULRL", pos = [0, -0.0625, -0.375], size = [0.125, 0.125, 0.75])
        pyrosim.Send_Joint(name = "ULRL_LLRL", parent = "ULRL", child = "LLRL", type = "revolute", position = [0, -0.0625, -0.675], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LLRL", pos = [0.25, 0, 0], size = [0.5, 0.125, 0.125])
        pyrosim.Send_Joint(name = "LLRL_LRF", parent = "LLRL", child = "LRF", type = "revolute", position = [0.4375, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LRF", pos = [0, 0, -0.125], size = [0.125, 0.125, 0.25])

        # Right Rear Leg
        pyrosim.Send_Joint(name = "Torso_URRL", parent = "Torso", child = "URRL", type = "revolute", position = [-0.5, 0.25, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "URRL", pos = [0, 0.0625, -0.375], size = [0.125, 0.125, 0.75])
        pyrosim.Send_Joint(name = "URRL_LRRL", parent = "URRL", child = "LRRL", type = "revolute", position = [0, 0.0625, -0.675], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LRRL", pos = [0.25, 0, 0], size = [0.5, 0.125, 0.125])
        pyrosim.Send_Joint(name = "LRRL_RRF", parent = "LRRL", child = "RRF", type = "revolute", position = [0.4375, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "RRF", pos = [0, 0, -0.125], size = [0.125, 0.125, 0.25])

        # Left Front Leg
        pyrosim.Send_Joint(name = "Torso_ULFL", parent = "Torso", child = "ULFL", type = "revolute", position = [0.5, -0.25, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "ULFL", pos = [0, -0.0625, -0.375], size = [0.125, 0.125, 0.75])
        pyrosim.Send_Joint(name = "ULFL_LLFL", parent = "ULFL", child = "LLFL", type = "revolute", position = [0, -0.0625, -0.675], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LLFL", pos = [0.25, 0, 0], size = [0.5, 0.125, 0.125])
        pyrosim.Send_Joint(name = "LLFL_LFF", parent = "LLFL", child = "LFF", type = "revolute", position = [0.4375, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LFF", pos = [0, 0, -0.125], size = [0.125, 0.125, 0.25])

        pyrosim.End()


    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "RFF")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "LRF")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "RRF")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "LFF")

        pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_URFL")
        pyrosim.Send_Motor_Neuron(name = 5, jointName = "Torso_ULFL")
        pyrosim.Send_Motor_Neuron(name = 6, jointName = "Torso_URRL")
        pyrosim.Send_Motor_Neuron(name = 7, jointName = "Torso_ULRL")
        pyrosim.Send_Motor_Neuron(name = 8, jointName = "URFL_LRFL")
        pyrosim.Send_Motor_Neuron(name = 9, jointName = "ULFL_LLFL")
        pyrosim.Send_Motor_Neuron(name = 10, jointName = "URRL_LRRL")
        pyrosim.Send_Motor_Neuron(name = 11, jointName = "ULRL_LLRL")
        pyrosim.Send_Motor_Neuron(name = 12, jointName = "LRFL_RFF")
        pyrosim.Send_Motor_Neuron(name = 13, jointName = "LLFL_LFF")
        pyrosim.Send_Motor_Neuron(name = 14, jointName = "LRRL_RRF")
        pyrosim.Send_Motor_Neuron(name = 15, jointName = "LLRL_LRF")


        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
#        print(str(self.myID) + "\t" + str(randomRow) + "\t" + str(randomColumn))
        self.weights[randomRow][randomColumn] = random.uniform(-1, 1)

    def Set_ID(self, ID):
        self.myID = ID
