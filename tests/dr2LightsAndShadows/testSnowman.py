# -*- coding: utf-8 -*-
# Laboratorio 3 Tests.py

#Import our gl library
import math
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from gllib.gl import Raytracer,colorScale
from gllib.material import Material
from gllib.sphere import Sphere
from gllib.light import PointLight,AmbientLight


#Material to use
button = Material(diffuse = colorScale(0, 0, 0),specularity=16)
eyePupil = Material(diffuse = colorScale(25/255, 25/255, 25/255),specularity=80)
snow = Material(diffuse = colorScale(1, 1, 1),specularity=32)
nose = Material(diffuse = colorScale(255/255, 135/255, 0),specularity=16)
smile = Material(diffuse = colorScale(65/255, 65/255, 65/255 ),specularity=16)
#Create our raytracer and spheres to build a snowman
raytracerGl=Raytracer(int(800/1),int(500/1))
raytracerGl.FOV = 120
raytracerGl.pointLight= PointLight(position=(-1,1,0),intensity=1.5)
raytracerGl.ambientLight= AmbientLight(strength=0.1)
raytracerGl.sceneObjects.append( Sphere((0, 6, -11), 4, snow) )
raytracerGl.sceneObjects.append( Sphere((0, 0, -10), 4, snow) )
raytracerGl.sceneObjects.append( Sphere((0, -6, -9), 4, snow) )
raytracerGl.sceneObjects.append( Sphere((0, 0, -4.99), 0.5, button) )
raytracerGl.sceneObjects.append( Sphere((0, -2, -4.99), 0.5, button) )
raytracerGl.sceneObjects.append( Sphere((0, -4, -4.99), 0.5, button) )
raytracerGl.sceneObjects.append( Sphere((0, 3.6, -4.99), 0.4, nose) )
raytracerGl.sceneObjects.append( Sphere((-0.5, 4.4, -4.99), 0.25, eyePupil) )
raytracerGl.sceneObjects.append( Sphere((0.5, 4.4, -4.99), 0.25, eyePupil) )
raytracerGl.sceneObjects.append( Sphere((-0.6, 3, -4.99), 0.2, smile) )
raytracerGl.sceneObjects.append( Sphere((-0.2, 2.8, -4.99), 0.2, smile) )
raytracerGl.sceneObjects.append( Sphere((0.2, 2.8, -4.99), 0.2, smile) )
raytracerGl.sceneObjects.append( Sphere((0.6, 3, -4.99), 0.2, smile) ) 
raytracerGl.rtRender()

raytracerGl.glFinish('./tests/dr2LightsAndShadows/snowman.bmp')




