import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, ID):
        if c.numHiddenNeurons != 0:
            self.motorWeights = np.random.rand(c.numHiddenNeurons, c.numMotorNeurons) * 2 - 1
            self.sensorWeights = np.random.rand(c.numHiddenNeurons, c.numSensorNeurons) * 2 - 1

        else:
            self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1

        if c.selfConnectNeurons:
            self.hiddenWeights = np.random.rand(c.numHiddenNeurons + c.numMotorNeurons) * 2 - 1

        if c.recurrentNeurons:
            self.recurrentWeights = np.random.rand(c.numMotorNeurons, c.numHiddenNeurons) * 2 - 1

        self.myID = ID
        self.age = 1


    def Start_Simulation(self, directOrGUI):
        self.Generate_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID) + " &")


    def Final_Simulation(self):
        self.Generate_Brain()
        os.system('"C:\OBSCommand\OBSCommand.exe" /startrecording')
        os.system("python simulate.py GUI " + str(self.myID))
        os.system('"C:\OBSCommand\OBSCommand.exe" /stoprecording')


    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

        file_read = False

        while not file_read:
            try:
                file = open("fitness" + str(self.myID) + ".txt", "r")
                file_read = True
            except PermissionError:
                time.sleep(0.01)

        self.fitness = file.read()
#        print(self.fitness)
        file.close()
#        print("fitness: " + str(self.fitness))
        os.system("del fitness" + str(self.myID) + ".txt")

        while not os.path.exists("footprints" + str(self.myID) + ".npy"):
            time.sleep(0.01)

        file_read = False

        while not file_read:
            try:
                feet = np.load("footprints" + str(self.myID) + ".npy")
                file_read = True
            except:
                time.sleep(0.01)

        self.footprints = feet

        os.system("del footprints" + str(self.myID) + ".npy")


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

        numNeurons = 0

        if c.numHiddenNeurons != 0:
            if c.targetsForSensors == []:
                for l in pyrosim.linkNamesToIndices:
                    pyrosim.Send_Sensor_Neuron(name = numNeurons, linkName = l)
                    numNeurons += 1
            else:
                for n in c.targetsForSensors:
                    pyrosim.Send_Sensor_Neuron(name = numNeurons, linkName = n)
                    numNeurons += 1

            for h in range(c.numHiddenNeurons):
                pyrosim.Send_Hidden_Neuron(name = numNeurons + h)

            numNeurons += c.numHiddenNeurons

            for m in pyrosim.jointNamesToIndices:
                pyrosim.Send_Motor_Neuron(name = numNeurons, jointName = m)
                numNeurons += 1

            for s in range(c.numSensorNeurons):
                for h in range(c.numHiddenNeurons):
                    pyrosim.Send_Synapse(sourceNeuronName = s, targetNeuronName = c.numSensorNeurons + h, weight = self.sensorWeights[h][s])

            for h in range(c.numHiddenNeurons):
                for m in range(c.numMotorNeurons):
                    pyrosim.Send_Synapse(sourceNeuronName = c.numSensorNeurons + h, targetNeuronName = c.numSensorNeurons + c.numHiddenNeurons + m, weight = self.motorWeights[h][m])

        else:
            for l in pyrosim.linkNamesToIndices:
                pyrosim.Send_Sensor_Neuron(name = numNeurons, linkName = l)
                numNeurons += 1

            for m in pyrosim.jointNamesToIndices:
                pyrosim.Send_Motor_Neuron(name = numNeurons, jointName = m)
                numNeurons += 1

            for s in range(c.numSensorNeurons):
                for m in range(c.numMotorNeurons):
                    pyrosim.Send_Synapse(sourceNeuronName = s, targetNeuronName = m + c.numSensorNeurons, weight = self.weights[s][m])

        if c.selfConnectNeurons:
            for m in range(c.numHiddenNeurons + c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = m + c.numSensorNeurons, targetNeuronName = m + c.numSensorNeurons, weight = self.hiddenWeights[m])

        if c.recurrentNeurons and c.numHiddenNeurons != 0:
            for m in range(c.numMotorNeurons):
                for h in range(c.numHiddenNeurons):
                     pyrosim.Send_Synapse(sourceNeuronName = m + c.numSensorNeurons + c.numHiddenNeurons, targetNeuronName = h + c.numSensorNeurons, weight = self.recurrentWeights[m][h])

        pyrosim.End()


    def Mutate(self):
        if c.numHiddenNeurons != 0:
            motorOrSensor = np.random.rand()

            if motorOrSensor > 0.5:
                self.sensorWeights[random.randint(0, c.numHiddenNeurons) - 1][random.randint(0, c.numSensorNeurons) - 1] = random.uniform(-1, 1)
            else:
                self.motorWeights[random.randint(0, c.numHiddenNeurons) - 1][random.randint(0, c.numMotorNeurons) - 1] = random.uniform(-1, 1)

        else:
            self.weights[random.randint(0, c.numSensorNeurons) - 1][random.randint(0, c.numMotorNeurons) - 1] = random.uniform(-1, 1)

        if c.selfConnectNeurons:
            if np.random.rand() > 0.5:
                self.hiddenWeights[random.randint(0, c.numHiddenNeurons + c.numMotorNeurons) - 1] = random.uniform(-1, 1)

        if c.recurrentNeurons and c.numHiddenNeurons != 0:
            if np.random.rand() > 0.5:
                self.recurrentWeights[random.randint(0, c.numMotorNeurons) -1][random.randint(0, c.numHiddenNeurons) - 1] = random.uniform(-1,1)


    def Set_ID(self, ID):
        self.myID = ID
