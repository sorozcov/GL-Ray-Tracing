# -*- coding: utf-8 -*-
# Laboratorio 3 Tests.py

#Import our gl library
import math
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from gllib.gl import Raytracer,colorScale
from gllib.material import Material
from gllib.sphere import Sphere
from gllib.obj import Texture


#Material to use
button = Material(diffuse = colorScale(0, 0, 0))
eyePupil = button
snow = Material(diffuse = colorScale(1, 1, 1))
nose = Material(diffuse = colorScale(255/255, 135/255, 0))
smile = Material(diffuse = colorScale(65/255, 65/255, 65/255 ))

#Create our raytracer and spheres to build a snowman
raytracerGl=Raytracer(800,500)

raytracerGl.sceneObjects.append( Sphere((0, 6, -11), 4, snow) )
raytracerGl.sceneObjects.append( Sphere((0, 0, -10), 4, snow) )
raytracerGl.sceneObjects.append( Sphere((0, -6, -9), 4, snow) )
raytracerGl.sceneObjects.append( Sphere((0, 0, -4.99), 0.5, button) )
raytracerGl.sceneObjects.append( Sphere((0, -2, -4.99), 0.5, button) )
raytracerGl.sceneObjects.append( Sphere((0, -4, -4.99), 0.5, button) )
raytracerGl.sceneObjects.append( Sphere((0, 3.6, -4.99), 0.4, nose) )
raytracerGl.sceneObjects.append( Sphere((-0.5, 4.4, -4.99), 0.2, eyePupil) )
raytracerGl.sceneObjects.append( Sphere((0.5, 4.4, -4.99), 0.2, eyePupil) )
raytracerGl.sceneObjects.append( Sphere((-0.6, 3, -4.99), 0.2, smile) )
raytracerGl.sceneObjects.append( Sphere((-0.2, 2.8, -4.99), 0.2, smile) )
raytracerGl.sceneObjects.append( Sphere((0.2, 2.8, -4.99), 0.2, smile) )
raytracerGl.sceneObjects.append( Sphere((0.6, 3, -4.99), 0.2, smile) ) 
raytracerGl.rtRender()

raytracerGl.glFinish('./tests/dr1Spheres/snowman.bmp')




