
# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 14/10/2020
#  Cone.py

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from gllib.mathgl import MathGl
import numpy as np
from numpy import arccos, arctan2 ,cos

#Intersect class to define the distance of intersection
class Intersect(object):
    def __init__(self, intersectDistance,point,normal,sceneObject=None,texCoords=None):

        self.distance = intersectDistance
        self.point = point
        self.normal = normal
        self.sceneObject = sceneObject
        self.texCoords=texCoords


#Class Cone to render a Cone object
#https://lousodrome.net/blog/light/2017/01/03/intersection-of-a-ray-and-a-cone/
class Cone(object):
    # Init with centerPoint, radius and material
    def __init__(self, yMin, yMax,posX=0,posY=0,posZ=-5,material=None):
        self.yMin = yMin
        self.yMax = yMax
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.material = material
        self.mathGl = MathGl()

    # Function to know if a a ray intersects the Cone 
    # Return intersect class object if intersection, else None
    def ray_intersect(self, origin, direction):
        
       
        # t es igual a la distancia en el rayo
        # P = O + tD
        # We need to calculate at**2 +bt+c=0 to find t
      
        a=direction[0]**2+direction[2]**2-direction[1]**2
        b=2*origin[0]*direction[0]+2*origin[2]*direction[2]-2*origin[1]*direction[1]
        c=origin[0]**2+origin[2]**2-origin[1]**2
        determinant=b**2-4*a*c
        if(determinant<0):
            return None
        elif(determinant==0):
            t0=(-b/(2*a))
        else:
            t0=(-b-determinant**1/2 )/(2*a)    
            t1=(-b+determinant**1/2 )/(2*a) 
            #If origin is behind cone
            if t0 < 0:
                t0=t1 #t0 with new Value t1

        if t0 < 0:
            return None
        point=self.mathGl.sumVector(origin,self.mathGl.scalarMultiplicationVector(direction,t0)) 
        #Check min and max
        if(point[1]<self.yMin or point[1]>self.yMax):
            return None
        normal=self.mathGl.subtractVector(point,[self.posX,self.posY,self.posZ])
        normal=self.mathGl.normalizeVector(normal)  
        return Intersect(intersectDistance = t0,point=point,normal=normal,sceneObject=self,texCoords=None)
        
        
