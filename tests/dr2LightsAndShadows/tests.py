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
from gllib.light import PointLight,AmbientLight


#Material to use
button = Material(diffuse = colorScale(0, 0, 0))
eyePupil = button
snow = Material(diffuse = colorScale(1, 1, 1))
nose = Material(diffuse = colorScale(255/255, 135/255, 0),specularity=64)
smile = Material(diffuse = colorScale(65/255, 65/255, 65/255 ),specularity=32)
blue = Material(diffuse = colorScale(120/255, 135/255, 200/255),specularity=16)
red = Material(diffuse = colorScale(190/255, 10/255, 10/255),specularity=128)
#Create our raytracer and spheres to build a snowman
raytracerGl=Raytracer(int(800/2),int(500/2))
raytracerGl.pointLight= PointLight(position=(-2,2,0),intensity=1.5)
raytracerGl.ambientLight= AmbientLight(strength=0.1)
raytracerGl.sceneObjects.append( Sphere((0, 0, -5), 1, nose))
raytracerGl.sceneObjects.append( Sphere((-0.5, 0.5, -3), 0.25, blue) )


raytracerGl.rtRender()

raytracerGl.glFinish('./tests/dr2LightsAndShadows/test.bmp')




