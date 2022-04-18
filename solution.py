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


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.End()


    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name = "Torso", pos = [0,0,1.5] , size = [0.25,0.375,0.75])

        pyrosim.Send_Joint(name = "Torso_Neck", parent = "Torso", child = "Neck", type = "revolute", position = [0,0,1.875], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "Neck", pos = [0, 0, 0.0625], size = [0.125,0.125,0.125])

        pyrosim.Send_Joint(name = "Neck_Head", parent = "Neck", child = "Head", type = "revolute", position = [0,0,0.125], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "Head", pos = [0, 0, 0.125], size = [0.25, 0.25, 0.25])

        pyrosim.Send_Joint(name = "Torso_LShoulder", parent = "Torso", child = "LShoulder", type = "revolute", position = [0,-0.1875, 1.875], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name = "LShoulder", pos = [0, -0.0025, 0], size = [0.005, 0.005, 0.005])

        pyrosim.Send_Joint(name = "LShoulder_LArm", parent = "LShoulder", child = "LArm", type = "revolute", position = [0, -0.0025, 0], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "LArm", pos = [0, -0.0625, -0.25], size = [0.125, 0.125, 0.5])

        pyrosim.Send_Joint(name = "LArm_LForearm", parent = "LArm", child = "LForearm", type = "revolute", position = [0, -0.0625, -0.5], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "LForearm", pos = [0, 0, -0.2], size = [0.125, 0.125, 0.4])

        pyrosim.Send_Joint(name = "Torso_RShoulder", parent = "Torso", child = "RShoulder", type = "revolute", position = [0,0.1875, 1.875], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name = "RShoulder", pos = [0, 0.0025, 0], size = [0.005, 0.005, 0.005])

        pyrosim.Send_Joint(name = "RShoulder_RArm", parent = "RShoulder", child = "RArm", type = "revolute", position = [0, 0.0025, 0], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "RArm", pos = [0, 0.0625, -0.25], size = [0.125, 0.125, 0.5])

        pyrosim.Send_Joint(name = "RArm_RForearm", parent = "RArm", child = "RForearm", type = "revolute", position = [0, 0.0625, -0.5], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "RForearm", pos = [0, 0, -0.2], size = [0.125, 0.125, 0.4])

        pyrosim.Send_Joint(name = "Torso_LHip", parent = "Torso", child = "LHip", type = "revolute", position = [0, 0.125, 1.125], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "LHip", pos = [0, 0, -0.0025], size = [0.005, 0.005, 0.005])

        pyrosim.Send_Joint(name = "LHip_LULeg", parent = "LHip", child = "LULeg", type = "revolute", position = [0, 0, -0.0025], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "LULeg", pos = [0, 0, -0.25], size = [0.125, 0.125, 0.5])

        pyrosim.Send_Joint(name = "LULeg_LLeg", parent = "LULeg", child = "LLeg", type = "revolute", position = [0, 0, -0.5], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "LLeg", pos = [0, 0, -0.25], size = [0.125, 0.125, 0.5])

        pyrosim.Send_Joint(name = "LLeg_LFoot", parent = "LLeg", child = "LFoot", type = "revolute", position = [0, 0, -0.5], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "LFoot", pos = [-0.1, 0, -0.0625], size = [0.4, 0.125, 0.125])

        pyrosim.Send_Joint(name = "Torso_RHip", parent = "Torso", child = "RHip", type = "revolute", position = [0, -0.125, 1.125], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "RHip", pos = [0, 0, -0.0025], size = [0.005, 0.005, 0.005])

        pyrosim.Send_Joint(name = "RHip_RULeg", parent = "RHip", child = "RULeg", type = "revolute", position = [0, 0, -0.0025], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "RULeg", pos = [0, 0, -0.25], size = [0.125, 0.125, 0.5])

        pyrosim.Send_Joint(name = "RULeg_RLeg", parent = "RULeg", child = "RLeg", type = "revolute", position = [0, 0, -0.5], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "RLeg", pos = [0, 0, -0.25], size = [0.125, 0.125, 0.5])

        pyrosim.Send_Joint(name = "RLeg_RFoot", parent = "RLeg", child = "RFoot", type = "revolute", position = [0, 0, -0.5], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name = "RFoot", pos = [-0.1, 0, -0.0625], size = [0.4, 0.125, 0.125])

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
