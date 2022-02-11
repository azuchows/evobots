from solution import SOLUTION
import constants
import copy
import os
import numpy as np
import copy
import random

class PARETO_OPTIMIZATION:
    def __init__(self):
        os.system("del fitness*")
        os.system("del brain*")

        self.nextAvailableID = 0
        self.population = {}
        self.populationSize = 0

        # initial population generation
        for individual in range(constants.goalPopulationSize):
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
        self.Crossover()
        self.Spawn()
        self.Evaluate(self.population, "DIRECT")
        self.Print(currentGeneration)
        self.Select()
        self.Age()


    def Crossover(self):
#        print(self.populationSize)
        self.children = {}

        # create new members of the population by crossover
        for p in range(self.populationSize):
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
            for r in range(constants.numSensorNeurons):
                for c in range(constants.numMotorNeurons):
                    if np.random.random() >= (1-constants.crossoverChance):
                        child.weights[r][c] = p1.weights[r][c]
                    else:
                        child.weights[r][c] = p2.weights[r][c]

            # chance to mutate a random weight
            if np.random.random() >= (1-constants.mutationChance):
                child.Mutate()

            if p1.age > p2.age:
                child.age = p1.age
            else:
                child.age = p2.age


        for c in self.children:
            self.population[self.populationSize] = self.children[c]
            self.populationSize = len(self.population)

#        print(self.population)


    def Spawn(self):
        for s in range(constants.numSpawn):
            self.population[self.populationSize] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.populationSize += 1


    def Evaluate(self, solutions, directOrGUI):
        for s in self.population:
            solutions[s].Start_Simulation(directOrGUI)

        for s in self.population:
            solutions[s].Wait_For_Simulation_To_End()


    def Print(self, currentGeneration):
        print("\n\nCurrent generation: " + str(currentGeneration))
        for i in self.population:
            print(str(self.population[i].fitness))
        print("")


    def Select(self):
        pass


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

#        np.savetxt("bestFit", self.parents[bestKey].weights, delimiter = '\t\t')
