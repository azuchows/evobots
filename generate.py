import pyrosim.pyrosim as pyrosim
import random
import constants as c
import os
import math

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5] , size=[1,1,1])

    pyrosim.End()

def Create_Robot():
    Generate_Body()
    Generate_Brain()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name = "Torso", pos = [0,0,1] , size = [1.5,0.5,0.25], rpy = [0, 0, 0])

    # Right Front Leg
    pyrosim.Send_Joint(name = "Torso_URFL", parent = "Torso", child = "URFL", type = "revolute", position = [0.5, 0.25, 1], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name = "URFL", pos = [0, 0.0625, -0.375], size = [0.125, 0.125, 0.75], rpy = [0, 0, 0])
    pyrosim.Send_Joint(name = "URFL_LRFL", parent = "URFL", child = "LRFL", type = "revolute", position = [0, 0.0625, -0.675], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name = "LRFL", pos = [0.25, 0, 0], size = [0.5, 0.125, 0.125])
    pyrosim.Send_Joint(name = "LRFL_RFF", parent = "LRFL", child = "RFF", type = "revolute", position = [0.4375, 0, 0], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name = "RFF", pos = [0, 0, -0.125], size = [0.125, 0.125, 0.25], rpy = [0, 0, 0])

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

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain0.nndf")

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
            pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, weight = random.uniform(-1,1))

    pyrosim.End()

Create_World()

Create_Robot()

os.system("python simulate.py GUI 0")
