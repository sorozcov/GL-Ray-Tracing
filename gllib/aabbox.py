
# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 04/09/2020
#  AABBox.py

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from gllib.mathgl import MathGl
from gllib.plane import Plane

#Intersect class to define the distance of intersection
class Intersect(object):
    def __init__(self, intersectDistance,point,normal,sceneObject=None,texCoords=None):

        self.distance = intersectDistance
        self.point = point
        self.normal = normal
        self.sceneObject = sceneObject
        self.texCoords=texCoords


#Class AABBox to render a AABBox object
#Axis Adjacent Bounding box
class AABBox(object):
    # Init with position,size and material
    def __init__(self, position, size, material):
        self.mathGl = MathGl()
        self.position = position
        if(len(self.position)<3):
            raise Exception("Sorry, no numbers below zero")
        self.size = size
        self.material = material
        self.planes = []
        halfSize=size/2
        #6 Planes x,y and z
        self.planes.append(Plane(position=self.mathGl.sumVector(position,(halfSize,0,0)),normal=(1,0,0),material=material))
        self.planes.append(Plane(position=self.mathGl.sumVector(position,(-halfSize,0,0)),normal=(-1,0,0),material=material))
        self.planes.append(Plane(position=self.mathGl.sumVector(position,(0,halfSize,0)),normal=(0,1,0),material=material))
        self.planes.append(Plane(position=self.mathGl.sumVector(position,(0,-halfSize,0)),normal=(0,-1,0),material=material))
        self.planes.append(Plane(position=self.mathGl.sumVector(position,(0,0,halfSize)),normal=(0,0,1),material=material))
        self.planes.append(Plane(position=self.mathGl.sumVector(position,(0,0,-halfSize)),normal=(0,0,-1),material=material))

        
        

    # Function to know if a a ray intersects the AABBox 
    # Return intersect class object if intersection, else None
    def ray_intersect(self, origin, direction):
        #Create boundingBox
        boundsMin=[0,0,0]
        boundsMax=[0,0,0]
        #To manage little error on bounds
        epsilon =0.001
        for i in range(3):
            boundsMin[i]=self.position[i]-((self.size+epsilon)/2)
            boundsMax[i]=self.position[i]+((self.size+epsilon)/2)
        t=float('inf')
        intersect=None
        #Check for intersects in each plane
        for plane in self.planes:
            planeIntersect = plane.ray_intersect(origin=origin,direction=direction)
            if planeIntersect is not None:
                isInside=True
                for i in range(3):
                    isInside=isInside and planeIntersect.point[i] >= boundsMin[i] and planeIntersect.point[i] <= boundsMax[i]
                isInside=isInside and planeIntersect.distance<t
                if(isInside):
                    t=planeIntersect.distance
                    intersect=planeIntersect
        if(intersect is None):
            return None
        return Intersect(intersectDistance = intersect.distance,point=intersect.point,normal=intersect.normal,sceneObject=self)

        
        
