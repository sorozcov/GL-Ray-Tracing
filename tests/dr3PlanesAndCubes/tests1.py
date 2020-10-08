# -*- coding: utf-8 -*-
# Laboratorio 3 Tests.py

#Import our gl library
import math
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from gllib.gl import Raytracer,colorScale
from gllib.material import Material,REFLECTIVE
from gllib.sphere import Sphere 
from gllib.plane import Plane
from gllib.aabbox import AABBox 
from gllib.obj import Texture
from gllib.light import PointLight,AmbientLight


#Material to use
color1 = Material(diffuse = colorScale(116/255, 47/255, 0),specularity=16)
color2 = Material(diffuse = colorScale(231/255, 228/255, 228/255),specularity=32)
color3 = Material(diffuse = colorScale(0.2,0.6,0.8),specularity=32)
color4 = Material(diffuse = colorScale(1, 1, 1),specularity=16)
color5 = Material(diffuse = colorScale(1, 0, 0),specularity=16)
color6 = Material(diffuse = colorScale(0, 1, 0),specularity=16)

#Create our raytracer 
raytracerGl=Raytracer(int(512/2),int(512/2))
raytracerGl.pointLight= PointLight(position=(0,1,-6),intensity=1)
raytracerGl.ambientLight= AmbientLight(strength=0.1)


#Planes
#Below
raytracerGl.sceneObjects.append( Plane(position=(0,-3,0),normal=(0,1,0),material=color4))
#Back
raytracerGl.sceneObjects.append( Plane(position=(0,0,-10),normal=(0,0,1),material=color4))
#Left
raytracerGl.sceneObjects.append( Plane(position=(-4,0,0),normal=(1,0,0),material=color2))
#Right
raytracerGl.sceneObjects.append( Plane(position=(4,0,0),normal=(-1,0,0),material=color2))
#Top
raytracerGl.sceneObjects.append( Plane(position=(0,3,0),normal=(0,-1,0),material=color4))


# AAABox
raytracerGl.sceneObjects.append( AABBox(position=(1,-1.5,-5),size=1,material=color5))
raytracerGl.sceneObjects.append( AABBox(position=(-0.8,-1.3,-4),size=1.2,material=color6))


raytracerGl.rtRender()

raytracerGl.glFinish('./tests/dr3PlanesAndCubes/test1.bmp')




