import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("tower.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5



for i in range(10):
    x = .90 ** i
    pyrosim.Send_Cube(name="Box", pos=[x,y,(z+i)] , size=[(length * x),(width * x),(height *x)])

pyrosim.End()
