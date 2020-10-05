
# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 04/09/2020
#  Plane.py

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from gllib.mathgl import MathGl

#Intersect class to define the distance of intersection
class Intersect(object):
    def __init__(self, intersectDistance,point,normal,sceneObject=None):

        self.distance = intersectDistance
        self.point = point
        self.normal = normal
        self.sceneObject = sceneObject


#Class Plane to render a Plane object
class Plane(object):
    # Init with position,normal and material
    def __init__(self, position, normal, material):
        self.mathGl = MathGl()
        self.position = position
        self.normal = self.mathGl.normalizeVector(normal)
        self.material = material
        

    # Function to know if a a ray intersects the Plane 
    # Return intersect class object if intersection, else None
    def ray_intersect(self, origin, direction):
        # P = O + tD
        # n1 = position-origin  dot normal
        # n2 direction dot normal
        # t = n1/n2
        n2= self.mathGl.dotProductVector(direction,self.normal)
        n1= self.mathGl.dotProductVector(self.mathGl.subtractVector(self.position,origin),self.normal)
        #When ray is parallel to plane
        if(abs(n2) > 0.0001):
            t=n1/n2
            if t>0:
                point=self.mathGl.sumVector(origin,self.mathGl.scalarMultiplicationVector(direction,t))
                return Intersect(intersectDistance = t,point=point,normal=self.normal,sceneObject=self)
        #Any other way there is no intersection
        return None

        
        
