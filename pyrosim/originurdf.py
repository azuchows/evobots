from pyrosim.commonFunctions import Save_Whitespace

class ORIGIN_URDF:

    def __init__(self,pos, rpy):

        self.depth  = 3

        posString = str(pos[0]) + " " + str(pos[1]) + " " + str(pos[2])

        rpyString = str(rpy[0]) + " " + str(rpy[1]) + " " + str(rpy[2])

        self.string = '<origin xyz="' + posString + '" rpy="' + rpyString + '"/>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string + '\n' )
