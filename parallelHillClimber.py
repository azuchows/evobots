from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del fitness*")
        os.system("del brain*")
        self.nextAvailableID = 0
        self.parents = {}

        for p in range(c.populationSize):
            self.parents[p] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        self.parents[0].Create_World()
        self.parents[0].Generate_Body()

    def Evolve(self):
        self.Evaluate(self.parents, "DIRECT")


        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation("DIRECT", currentGeneration)

    def Evolve_For_One_Generation(self, directOrGUI, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, "DIRECT")
        self.Print(currentGeneration)
        self.Select(self.children)

    def Spawn(self):
        self.children = {}

        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])

            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()


    def Select(self, children):
        for parent in self.parents:
            if float(self.parents[parent].fitness) < float(self.children[parent].fitness):
                self.parents[parent] = self.children[parent]

    def Print(self, currentGeneration):
        print("\n\nCurrent generation: " + str(currentGeneration))
        for parent in self.parents:
            print("Parent fitness: " + str(self.parents[parent].fitness) + "\tChild fitness: " + str(self.children[parent].fitness))
        print("")

    def Show_Best(self):
        bestFit = -1000
        bestKey = 0

        for parent in self.parents:
            if float(self.parents[parent].fitness) > bestFit:
                bestFit = float(self.parents[parent].fitness)
                bestKey = parent

        print(self.parents[bestKey].fitness)
        self.parents[bestKey].Final_Simulation()

#        np.savetxt("bestFit", self.parents[bestKey].weights, delimiter = '\t\t')


    def Evaluate(self, solutions, directOrGUI):
        for s in range(c.populationSize):
            solutions[s].Start_Simulation(directOrGUI)

        for s in range(c.populationSize):
            solutions[s].Wait_For_Simulation_To_End()
