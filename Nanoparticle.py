from ase.cluster.cubic import FaceCenteredCubic
import numpy as np

class BoundingBox:
    def __init__(self, w, h, l, position):
        self.xExtent = w
        self.yExtent = l
        self.zExtent = h

        self.position = position

    def translate(self, displacement):
        self.position = self.position + displacement

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
            self.position[1] = self.position[1] - self.yExtent
        if(aroundYAxis):
            swap(self.xExtent, self.zExtent)
            self.position[2] = self.position[2] - self.zExtent
        if(aroundZAxis):
            swap(self.xExtent, self.yExtent)
            self.position[0] = self.position[0] + self.xExtent

class Nanoparticle(FaceCenteredCubic):
    def __init__(self, surfaces, layers, latticeConstant, atomicSymbols):
        super().init(atomicSymbols[0], surfaces, layers, latticeConstant)

        self.boundingBox = findBoundingBox()

    def findBoundingBox(self):
        positions = self.get_positions()

        minima = [1e10, 1e10, 1e10]
        maxima = [-1e10, -1e10, -1e10]

        for position in position:
            for coordinate in range(3):
                if(minima[coordinate] > position[coordinate]):
                    minima[coordinate] = position[coordinate]
                if(maxima[coordinate] < position[coordinate]):
                    maxima[coordinate] = position[coordinate]

        w = maxima[0] - minima[0]
        l = maxima[1] - minima[1]
        h = maxima[2] - minima[2]

        return BoundingBox(w, h, l, minima[0], minima[1], minima[2])

    def translate(self, displacement):
        super.translate(displacement)
        self.boundingBox.translate(displacement)


    def alignParticles(self, otherNanoparticle):
        #TODO Align also rotation and not only orientation
        otherAnchorPoint = otherNanoparticle.boundingBox.position
        ownAnchorPoint = self.boundingBox.position

        displacement = otherAnchorPoint - ownAnchorPoint
        otherNanoparticle.translate(displacement)
