# -*- coding: utf-8 -*-
# Project Ray Tracing

#Import our gl library
import math
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from gllib.gl import Raytracer,colorScale
from gllib.material import Material,REFLECTIVE
from gllib.sphere import Sphere 
from gllib.plane import Plane
from gllib.disc import Disc
from gllib.cone import Cone
from gllib.aabbox import AABBox 
from gllib.obj import Texture,Envmap
from gllib.light import PointLight,AmbientLight


#Material to use


colorRed = Material(diffuse = colorScale(1, 0, 0),specularity=16)
colorBlack = Material(diffuse = colorScale(34/255, 24/255, 12/255),specularity=16)
colorBrown = Material(diffuse = colorScale(106/255, 59/255, 0/255),specularity=16)
colorYellow = Material(diffuse = colorScale(255/255, 255/255, 66/255),specularity=16)
blood = Material(diffuse = colorScale(175/255, 4/255, 4/255 ),specularity=120)
colorGray = Material(diffuse = colorScale(163/255, 179/255, 209/255 ),specularity=1024)
colorGray2 = Material(diffuse = colorScale(163/255, 179/255, 209/255 ),specularity=2048)
colorWhite = Material(diffuse = colorScale(255/255, 255/255, 255/255 ),specularity=1024)
mirror = Material(diffuse = colorScale(0.8, 0.8, 0.8),specularity=1024,matType=REFLECTIVE)
sunMat = Material(texture = Texture('./tests/project/sun.bmp'))


#Create our raytracer and spheres to build a snowman
raytracerGl=Raytracer(int(512),int(512))
raytracerGl.pointLight= PointLight(position=(0,0,0),intensity=1)
raytracerGl.ambientLight= AmbientLight(strength=0.2)
raytracerGl.envmap = Envmap('./tests/project/night.bmp')


# Spheres Sun
raytracerGl.sceneObjects.append( Sphere((-10, 13, -30), 2, sunMat))


# Reflection Espejo
raytracerGl.sceneObjects.append( AABBox(position=(0.5,0,-15),size=4.4,material=mirror))
#Blood
raytracerGl.sceneObjects.append( Disc(center=(0,-1.6,-5.1),normal=(0,1,0),radius=1.2,material=colorRed))


# #Planes
# #Floor
raytracerGl.sceneObjects.append( Plane(position=(0,-8,0),normal=(0,1,0),material=colorGray))


#Among us RED
#Legs
raytracerGl.sceneObjects.append( AABBox(position=(1+0.6,-1.3,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0,-1.3,-5),size=0.3,material=colorRed))
#Body
raytracerGl.sceneObjects.append( AABBox(position=(1+0.6,-1,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0.3,-1,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0,-1,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0.6,-0.7,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0.3,-0.7,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0,-0.7,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0.6,-0.4,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0.3,-0.4,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0,-0.4,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0.6,-0.1,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0.3,-0.1,-5),size=0.3,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0,-0.1,-5),size=0.3,material=colorRed))
#Head
raytracerGl.sceneObjects.append( AABBox(position=(1+0.5,0.2,-5),size=0.4,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0.1,0.2,-5),size=0.4,material=colorRed))
#Eyes
raytracerGl.sceneObjects.append( AABBox(position=(1+0.05,0,-5),size=0.5,material=colorGray2))

#Backpack
raytracerGl.sceneObjects.append( AABBox(position=(1+0.95,-0.2,-5.0),size=0.2,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0.95,-0.4,-5.0),size=0.2,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0.95,-0.6,-5.0),size=0.2,material=colorRed))
raytracerGl.sceneObjects.append( AABBox(position=(1+0.95,-0.8,-5.0),size=0.2,material=colorRed))

# #Hat
raytracerGl.sceneObjects.append( AABBox(position=(0.8+0.9,0.45,-4.8),size=0.3,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(0.8+0.6,0.45,-4.8),size=0.3,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(0.8+0.00,0.45,-4.8),size=0.3,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(0.8+0.3,0.45,-4.8),size=0.3,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(0.8+0.3,0.65,-4.8),size=0.3,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(0.8+0.6,0.65,-4.8),size=0.3,material=colorBlack))

#Among us YELLOW
# Legs
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.6,-1.3,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0,-1.3,-5),size=0.3,material=colorYellow))
#Body
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.6,-1,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.3,-1,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0,-1,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.6,-0.7,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.3,-0.7,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0,-0.7,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.6,-0.4,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.3,-0.4,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0,-0.4,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.6,-0.1,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.3,-0.1,-5),size=0.3,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0,-0.1,-5),size=0.3,material=colorYellow))
#Head
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.5,0.2,-5),size=0.4,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.1,0.2,-5),size=0.4,material=colorYellow))
#Balloon
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.35,0.4,-5),size=0.1,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.35,0.5,-5),size=0.1,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.35,0.6,-5),size=0.1,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.35,0.7,-5),size=0.1,material=colorBlack))
raytracerGl.sceneObjects.append( Sphere((-1-0.35, 0.85, -5), 0.3, colorYellow))
#Eyes
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.05,0,-5),size=0.5,material=colorGray2))

#Backpack
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.95,-0.2,-5.0),size=0.2,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.95,-0.4,-5.0),size=0.2,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.95,-0.6,-5.0),size=0.2,material=colorYellow))
raytracerGl.sceneObjects.append( AABBox(position=(-1-0.95,-0.8,-5.0),size=0.2,material=colorYellow))


# #Among us BLACK dead
#Legs
raytracerGl.sceneObjects.append( AABBox(position=(-0-0.6,-1.6,-5),size=0.3,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(-0-0,-1.6,-5),size=0.3,material=colorBlack))
#Body
raytracerGl.sceneObjects.append( AABBox(position=(-0-0.6,-1.3,-5),size=0.3,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(-0-0.3,-1.3,-5),size=0.3,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(-0-0,-1.3,-5),size=0.3,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(-0-0.6,-1,-5),size=0.3,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(-0-0.3,-1,-5),size=0.3,material=colorBlack))
raytracerGl.sceneObjects.append( AABBox(position=(-0-0,-1,-5),size=0.3,material=colorBlack))
#Bone
raytracerGl.sceneObjects.append( AABBox(position=(-0-0.35,-0.7,-5),size=0.2,material=colorWhite))
raytracerGl.sceneObjects.append( AABBox(position=(-0-0.35,-0.5,-5),size=0.2,material=colorWhite))
raytracerGl.sceneObjects.append( Sphere((-0-0.25,-0.3, -5), 0.2, colorWhite))
raytracerGl.sceneObjects.append( Sphere((-0-0.45, -0.3, -5), 0.2, colorWhite))




raytracerGl.rtRender()
raytracerGl.glFinish('./tests/project/projectSceneFinal.bmp')




