
# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 04/09/2020
#  Disc.py

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from gllib.mathgl import MathGl

#Intersect class to define the distance of intersection
class Intersect(object):
    def __init__(self, intersectDistance,point,normal,sceneObject=None,texCoords=None):

        self.distance = intersectDistance
        self.point = point
        self.normal = normal
        self.sceneObject = sceneObject
        self.texCoords=texCoords


#Class Disc to render a Disc object
class Disc(object):
    # Init with center,normal and material
    def __init__(self, center, normal,radius, material):
        self.mathGl = MathGl()
        self.center = center
        self.radius = radius
        self.normal = self.mathGl.normalizeVector(normal)
        self.material = material

        

    # Function to know if a a ray intersects the Disc 
    # Return intersect class object if intersection, else None
    #https://www.cl.cam.ac.uk/teaching/1999/AGraphHCI/SMAG/node2.html#SECTION00023700000000000000
    def ray_intersect(self, origin, direction):
        # P = O + tD
        # n1 = center-origin  dot normal
        # n2 direction dot normal
        # t = n1/n2
        n2= self.mathGl.dotProductVector(direction,self.normal)
        n1= self.mathGl.dotProductVector(self.mathGl.subtractVector(self.center,origin),self.normal)
        #When ray is parallel to Disc
        if(abs(n2) > 0.0001):
            t=n1/n2
            if t>0:
                point=self.mathGl.sumVector(origin,self.mathGl.scalarMultiplicationVector(direction,t))
                pointCenter =self.mathGl.subtractVector(point,self.center)
                dot = self.mathGl.dotProductVector(pointCenter,pointCenter)
                if(dot<self.radius**2):
                    return Intersect(intersectDistance = t,point=point,normal=self.normal,sceneObject=self)
        #Any other way there is no intersection
        return None

        
        
