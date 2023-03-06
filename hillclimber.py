from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")

        for currentGeneration in range(c.numberOfGenerations):
            print("Current generation number: " + str(currentGeneration))
            self.Evolve_For_One_Generation("DIRECT")

    def Evolve_For_One_Generation(self, directOrGUI):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(directOrGUI)
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        if (float(self.parent.fitness) < float(self.child.fitness)):
            print("Selected parent!\n")
        else:
            self.parent = self.child
            print("Selected child!\n")

    def Print(self):
        print("\n\nParent fitness: " + str(self.parent.fitness) + "\tChild fitness: " + str(self.child.fitness))

    def Show_Best(self):
        self.parent.Evaluate("GUI")
