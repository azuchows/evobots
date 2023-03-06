maxForce = 30
sleepInt = 1/120

STEPS = 1000

gravity = -9.8

numberOfGenerations = 500

numSpawn = 1

initialPopulationSize = 10
targetPopulationSize = 10

targetsForSensors = []
numSensorNeurons = 13
numMotorNeurons = 12
numHiddenNeurons = 10
recurrentNeurons = True
selfConnectNeurons = True


motorJointRange = 0.5

crossoverChance = 0.5

mutationChance = 0.05

forcedRoundMaximum = 10000

numChildren = 10

population = 'A'

if population == 'A':
    numHiddenNeurons = 4
    recurrentNeurons = True
    selfConnectNeurons = True

elif population == 'B':
    numHiddenNeurons = 20
    recurrentNeurons = False
    selfConnectNeurons = False

elif population == 'C':
    numHiddenNeurons = 0
    recurrentNeurons = False
    selfConnectNeurons = True

elif population == 'D':
    numHiddenNeurons = 0
    recurrentNeurons = False
    selfConnectNeurons = False
