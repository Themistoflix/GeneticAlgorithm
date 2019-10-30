

class BoundingBox:
    def __init__(self, w, h, l, x, y, z):
        self.xExtent = w
        self.yExtent = l
        self.zExtent = h

        self.x = x
        self.y = y
        self.z = z

    def translate(self, dx, dy, dz):
        self.x = self.x + dx
        self.y = self.y + dy
        self.z = self.z + dz

    def rotate90Clockwise(self, aroundXAxis, aroundYAxis, aroundZAxis):
        def swap(a, b):
            tmp = a
            a = b
            b = tmp

        #make sure, that the bounding box is correctly aligned to the molecule
        #Since xExtent, yExtent and zExtent are positive we have to move the
        #anchor point when rotating.
        if(aroundXAxis):
            swap(self.yExtent, self.zExtent)
            self.y = self.y - self.yExtent
        if(aroundYAxis):
            swap(self.xExtent, self.zExtent)
            self.z = self.z - self.zExtent
        if(aroundZAxis):
            swap(self.xExtent, self.yExtent)
            self.x = self.x + self.xExtent


class FCCLattice:
    #Use a righthanded cartesian coordinate system with only positive coordinates
    #width  is associated with the x component
    #lenght is associated with the y component
    #height is associated with the z component
    def __init__(self, width, length, height, latticeConstant):
        self.width  = width
        self.length = length
        self.height = height
        self.latticeConstant = latticeConstant

    def getIndexFromPosition(self, x, y, z):
        def indexInXYPlane(self, x, y):
            if(x % 2 == 0):
                return (y/2)*self.width + (y/2)*(self.width -1) + (x/2)
            else:
                return (y + 1)/2*self.width + (y - 1)*(self.width -1) + (x - 1)/2

        latticePointsPerLayer = self.width*self.length + (self.width - 1)*(self.length - 1)
        index = z*latticePointsPerLayer + indexInXYPlane(x, y)

        return index

    def getPositionFromIndex(self, index):
        def positionFromPlaneIndex(self, planeIndex):
            #a 'full block' is a row with length and the following row with lenght w -1
            fullBlocksAbove = int(index/(w + w-1))
            #shift the index into the first block
            index = index - fullBlocksAbove*(w + w-1)

            #check in which row the index is
            if(index > self.width -1):
                y = 1
            else:
                y = 0

            if(y == 0): #upper row, with lenght=self.width
                x = index*2
            else: #lower row, with lenght=self.width -1
                index = index - self.width +1
                x = index*2 -1

            return x, y


        latticePointsPerLayer = self.width*self.length + (self.width - 1)*(self.length - 1)
        z = int(index/latticePointsPerLayer)

        planeIndex = index - z*latticePointsPerLayer
        x, y = positionFromPlaneIndex(planeIndex)

        return x, y, z

class Nanoparticle:
    def __init__(self, lattice):
        self.lattice = lattice

        self.boundingBox        = BoundingBox()
        self.indices            = []
        self.positionsOnLattice = []
        self.atomNumbers        = []

    def findBoundingBox(self):

    def generate(self, particleNumber):

    def align(self, otherNanoparticle):

    def translate(self, dx, dy, dz):

    def rotate90Clockwise(self, aroundXAxis, self.aroundYAxis, self.aroundZAxis):

    def getAtoms(self)
