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

color1 = Material(diffuse = colorScale(0.8, 0.4, 0.25),specularity=16)
color2 = Material(diffuse = colorScale(0.4, 0.4, 0.4),specularity=32)
color3 = Material(diffuse = colorScale(0.2,0.6,0.8),specularity=32)

#Create our raytracer and spheres to build a snowman
raytracerGl=Raytracer(int(512/2),int(512/2))
raytracerGl.pointLight= PointLight(position=(0,0,0),intensity=1)
raytracerGl.ambientLight= AmbientLight(strength=0.1)
# raytracerGl.glClearColorScaleRGB(0.2,0.6,0.8)
# Spheres
# raytracerGl.sceneObjects.append( Sphere((1, 1, -8), 1.5, color1))
# raytracerGl.sceneObjects.append( Sphere((0, 0, -5), 0.5, color2))
# raytracerGl.sceneObjects.append( Sphere((-3, 3, -10), 2, mirror))
# raytracerGl.sceneObjects.append( Sphere((-3, -3, -10), 1, mirror))


#Planes
# raytracerGl.sceneObjects.append( Plane(position=(0,-10,0),normal=(0,1,0),material=color1))
raytracerGl.sceneObjects.append( Plane(position=(0,0,-10),normal=(0,0,1),material=color2))
raytracerGl.sceneObjects.append( Plane(position=(0,-5,-5),normal=(1,0,0),material=color2))

# AAABox
# raytracerGl.sceneObjects.append( AABBox(position=(1.5,-1.5,-5),size=1.5,material=color3))
# raytracerGl.sceneObjects.append( AABBox(position=(-1.5,-1.5,-5),size=1.5,material=color1))


raytracerGl.rtRender()

raytracerGl.glFinish('./tests/dr3PlanesAndCubes/test.bmp')




