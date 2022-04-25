from solution import SOLUTION
import constants
import copy
import os
import numpy as np
import copy
import random
import matplotlib.pyplot as plt


class PARETO_OPTIMIZATION:
    def __init__(self):
        os.system("del fitness*")
        os.system("del brain*")
        os.system("del tmp*.npy")

        self.nextAvailableID = 0
        self.population = {}
        self.populationSize = 0
        self.ages = []
        self.fitnesses = []
        self.generations = []

        # initial population generation
        for individual in range(constants.initialPopulationSize):
            self.population[individual] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        self.populationSize = len(self.population)

        # generate shared body and world files
        self.population[0].Create_World()
        self.population[0].Generate_Body()


    # begin evolution
    def Evolve(self):
        # determine fitness of initial generation - NEEDED?
#        self.Evaluate(self.population, "DIRECT")

        for currentGeneration in range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation("DIRECT", currentGeneration)


    def Evolve_For_One_Generation(self, directOrGUI, currentGeneration):
        try:
#        print(self.populationSize)
            self.Crossover()
#        print(self.populationSize)
            self.Spawn()
#        print(self.populationSize)
            self.Evaluate(self.population, directOrGUI)
            self.Print(currentGeneration)
            self.Store(currentGeneration)
#        for individual in self.population:
#            print(self.population[individual].age)
            self.Select()
            self.Print(currentGeneration, True)
        except MemoryError:
            self.Show_Best()
            exit()

    def Store(self, currentGeneration):
        for s in self.population:
            self.ages.append(int(self.population[s].age))
            self.fitnesses.append(-1 * float(self.population[s].fitness))
            self.generations.append(int(currentGeneration))


    def Crossover(self):
#        print(self.populationSize)
        self.children = {}

        # create new members of the population by crossover
        for p in range(constants.numChildren):
#            print(self.population)

            # picking parents
            p1 = random.choice(list(self.population))
            p2 = random.choice(list(self.population))

            #make sure that the parents are distinct
            while p2 == p1:
                p2 = random.choice(list(self.population))

            p1 = self.population[p1]
            p2 = self.population[p2]

            # create a a child
            child = SOLUTION(self.nextAvailableID)
            self.children[p] = child
            self.nextAvailableID += 1

            # assign weights from both parents by crossover
            if constants.numHiddenNeurons != 0:
                for h in range(constants.numHiddenNeurons):
                    for s in range(constants.numSensorNeurons):
                        if np.random.random() >= (1-constants.crossoverChance):
                            child.sensorWeights[h][s] = p1.sensorWeights[h][s]
                        else:
                            child.sensorWeights[h][s] = p2.sensorWeights[h][s]
                    for m in range(constants.numMotorNeurons):
                        if np.random.random() >= (1-constants.crossoverChance):
                            child.motorWeights[h][m] = p1.motorWeights[h][m]
                        else:
                            child.motorWeights[h][m] = p2.motorWeights[h][m]

            else:
                for s in range(constants.numSensorNeurons):
                    for m in range(constants.numMotorNeurons):
                        if np.random.random() >= (1-constants.crossoverChance):
                            child.weights[s][m] = p1.weights[s][m]
                        else:
                            child.weights[s][m] = p2.weights[s][m]

            if constants.selfConnectNeurons:
                for n in range(constants.numMotorNeurons + constants.numHiddenNeurons):
                    if np.random.random() >= (1 - constants.crossoverChance):
                        child.hiddenWeights[n] = p1.hiddenWeights[n]
                    else:
                        child.hiddenWeights[n] = p2.hiddenWeights[n]

            if constants.recurrentNeurons and constants.numHiddenNeurons != 0:
                for m in range(constants.numMotorNeurons):
                    for h in range(constants.numHiddenNeurons):
                        if np.random.random() >= (1 - constants.crossoverChance):
                            child.recurrentWeights[m][h] = p1.recurrentWeights[m][h]
                        else:
                            child.recurrentWeights[m][h] = p2.recurrentWeights[m][h]

            # chance to mutate a random weight
            if np.random.random() >= (1-constants.mutationChance):
                child.Mutate()

            if p1.age > p2.age:
                child.age = p1.age
            else:
                child.age = p2.age

        # increase age of parents
        self.Age()

        # combine child and total populations
        for c in self.children:
            self.population[self.children[c].myID] = self.children[c]
            self.populationSize = len(self.population)

#        print(self.population)


    def Spawn(self):
        for s in range(constants.numSpawn):
            self.population[self.nextAvailableID] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.populationSize += 1


    def Evaluate(self, solutions, directOrGUI):
        for s in self.population:
            solutions[s].Start_Simulation(directOrGUI)

        for s in self.population:
            solutions[s].Wait_For_Simulation_To_End()


    def Print(self, currentGeneration, select = False):
        if not select:
            print("\n\nCurrent generation: " + str(currentGeneration))
        else:
            print("\n\nSelected population for generation: " + str(currentGeneration))
        for i in self.population:
            print(str(self.population[i].fitness))
        print("")


    def Select(self):
        r = 0
        while self.populationSize > constants.targetPopulationSize and r <= constants.forcedRoundMaximum:
            competitor_one = self.population.pop(random.choice(list(self.population)))
            competitor_two = self.population.pop(random.choice(list(self.population)))

            if float(competitor_one.fitness) < float(competitor_two.fitness) and competitor_one.age < competitor_two.age:
                self.population[competitor_one.myID] = competitor_one

            elif float(competitor_two.fitness) < float(competitor_one.fitness) and competitor_two.age < competitor_one.age:
                self.population[competitor_two.myID] = competitor_two

            elif float(competitor_one.fitness) == float(competitor_two.fitness):
                if competitor_one.age < competitor_two.age:
                    self.population[competitor_one.myID] = competitor_one
                else:
                    self.population[competitor_two.myID] = competitor_two


            else:
                self.population[competitor_one.myID] = competitor_one
                self.population[competitor_two.myID] = competitor_two

            self.populationSize = len(self.population)

            r += 1
#            print(self.populationSize)


    def Age(self):
        for p in self.population:
            self.population[p].age += 1


    def Show_Best(self):
        bestFit = 1000
        bestKey = 0

        for i in self.population:
            if float(self.population[i].fitness) < bestFit:
                bestFit = float(self.population[i].fitness)
                bestKey = i

        print(self.population[bestKey].fitness)
        self.population[bestKey].Final_Simulation()

        footprints = self.population[bestKey].footprints

        af = np.array([self.ages, self.fitnesses])
        gf = np.array([self.generations, self.fitnesses])

        np.save("fitB", af)
        np.save("gFitB", gf)

        np.save("feetB", footprints)
