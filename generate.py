import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("castle.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5



for i in range(6):
    for j in range(6):
        for k in range(10):
            h = .90 ** k
            pyrosim.Send_Cube(name="Box", pos=[(x+i),(y+j),(z+k)] , size=[(length * h),(width * h),(height *h)])

pyrosim.End()
