
# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 04/09/2020
#  Sphere.py

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from gllib.mathgl import MathGl
import numpy as np
from numpy import arccos, arctan2 

#Intersect class to define the distance of intersection
class Intersect(object):
    def __init__(self, intersectDistance,point,normal,sceneObject=None,texCoords=None):

        self.distance = intersectDistance
        self.point = point
        self.normal = normal
        self.sceneObject = sceneObject
        self.texCoords=texCoords


#Class Sphere to render a sphere object
class Sphere(object):
    # Init with centerPoint, radius and material
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material
        self.mathGl = MathGl()

    # Function to know if a a ray intersects the sphere 
    # Return intersect class object if intersection, else None
    def ray_intersect(self, origin, direction):
        
        # https://www.scratchapixel.com/images/upload/ray-simple-shapes/raysphereisect1.png?
        # https://www.scratchapixel.com/images/upload/ray-simple-shapes/rayspherecases.png?
        # t es igual a la distancia en el rayo
        # P = O + tD
        # P0 = O + t0 * D
        # P1 = O + t1 * D
        #d va a ser la magnitud de un vector que es
        #perpendicular entre el rayo y el centro de la esfera
        # d > radio, el rayo no intersecta
        #tca es el vector que va del orign al punto perpendicular al centro
        # L vector from origin O to center C
        # OPP vector from origin O to PP perpendicular point to O and C 
        distanceOC = self.mathGl.subtractVector(self.center, origin)
        distanceOPP = self.mathGl.dotProductVector(distanceOC, direction)
        magnitudeOC = self.mathGl.magnitudeVector(distanceOC) # magnitud de L
        #This way we can calculate the distance from center C to PP.
       
        distanceCPP = (magnitudeOC**2 - distanceOPP**2) ** 0.5
        # If distanceCPP>radius then outside circle
        if distanceCPP > self.radius:
            return None

        # We calculate the distance from PP to I, the first intersection point with the circle. We need to apply pythagoras theorem with radius and distanceCPP
        distancePPI  = (self.radius ** 2 - distanceCPP**2) ** 0.5
        t0 = distanceOPP - distancePPI 
        t1 = distanceOPP + distancePPI 
        
        #If origin is behind sphere
        if t0 < 0:
            t0=t1 #t0 with new Value t1

        if t0 < 0:
            return None
            
        # We get the point value
        # P=O+tD
        point=self.mathGl.sumVector(origin,self.mathGl.scalarMultiplicationVector(direction,t0))
        normal=self.mathGl.subtractVector(point,self.center)
        normal=self.mathGl.normalizeVector(normal)


        u = 1 - (arctan2( normal[2], normal[0]) / (2 * np.pi) + 0.5)
        v =  arccos(-normal[1]) / np.pi

        tCoords = [u, v]
        #Any other way there is an intersection with distance t0
        return Intersect(intersectDistance = t0,point=point,normal=normal,sceneObject=self,texCoords=tCoords)
