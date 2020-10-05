# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 30/07/2020
#  gl.py

#Import struct to have c# alike structures with memory defined
import struct
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#We import our object class to gl.py
from gllib.obj import Obj,Texture
from gllib.mathgl import MathGl
from gllib.material import OPAQUE,TRANSPARENT,REFLECTIVE
from math import pi,cos,sin,tan



#char 1 byte
def char(var):
    return struct.pack('=c',var.encode('ascii'))

#word 2 bytes
def word(var):
    return struct.pack('=h',var)

#double word 4 bytes
def dword(var):
    return struct.pack('=l',var)

#double double word 8 bytes
def ddword(var):
    return struct.pack('=q',var)

#color function ro return rgb in bytes
def color(r,g,b):
    return bytes([b,g,r])

#color function ro return rgb in bytes
def colorScale(r,g,b):
    return bytes([round(b*255),round(g*255),round(r*255)])

maxRecursionDepth = 3 
#class Raytracer
class Raytracer(object):
    #Inititalize function glInit
    #Takes width and height to initialize, also the color
    def __init__(self,width,height,color=None):
        self.glInit(width,height,color)

    def glInit(self,width,height,color=None):
        self.mathGl = MathGl()
        self.glCreateWindow(width,height)
        self.currentColor = colorScale(1,1,1) if color==None else color
        self.glClear()
        self.glViewPort(0,0,width-1,height-1)
        self.FOV = 60
        self.camPosition=[0,0,0]
        self.sceneObjects = []
        self.pointLight=None
        self.ambientLight = None
    
    #Size of image result
    def glCreateWindow(self,width,height):
        self.width = width
        self.height = height
    
    #Change Viewport position and matrix
    def glViewPort(self,x, y, width, height):
        if(x>=self.width or y>=self.height):
            return False
        if(x+width>=self.width or y+height>=self.height):
            return False
        #We save the data necessary for the viewPort
        self.viewPortWidth= width
        self.viewPortHeight = height
        self.viewPortX = x
        self.viewPortY = y
        #Viewport matrix
        self.viewPortMatrix = [[width/2, 0, 0, x + width/2],
                                      [0, height/2, 0, y + height/2],
                                      [0, 0, 0.5, 0.5],
                                      [0, 0, 0, 1]]
        return True

    #Clear to set bitmap of one color default black
    def glClear(self):
        #Set to black 
        self.glClearColorScaleRGB(0,0,0)

    #Set bitmap to specif color
    def glClearColorScaleRGB(self,r,g,b):
        self.backgroundColor = colorScale(r,g,b)
        #Basically painting background
        # for x in range(self.width):
        #     for y in range(self.height):
        #         self.pixels[x][y]=colorPixels
        # Easier to use nested list comprenhension
        #https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
        
        #All pixels x,y
        self.pixels= [[self.backgroundColor for x in range(self.width)] for y in range(self.height)]

        #Zbuffer depth z
        self.zbuffer = [ [ float('inf') for x in range(self.width)] for y in range(self.height) ]

    #Clear with a background image to our scene
    def glClearBackground(self,filenameBackground):
        background = Texture(filenameBackground)
        # self.backgroundColor = colorScale(r,g,b)
        #Basically painting background
        for x in range(self.width):
            for y in range(self.height):
                b,g,r=background.getTextureCoordinates(x/self.width,y/self.height)
                self.pixels[x][y]=colorScale(r/255,g/255,b/255)
        # Easier to use nested list comprenhension
        #https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
        
        #All pixels x,y
        # self.pixels= [[self.backgroundColor for x in range(self.width)] for y in range(self.height)]

        #Zbuffer depth z
        self.zbuffer = [ [ float('inf') for x in range(self.width)] for y in range(self.height) ]

    #Functions to create points as absolute position
    def glVertexRGBAbsolute(self,x,y,r,g,b):

        self.pixels[y][x]=colorScale(r,g,b)

    def glVertexColorAbsolute(self,x,y,color=None):
        try:
            self.pixels[y][x]=self.currentColor if color == None else color
           
        except:
            #If tries to draw outside scren
            pass

    #Functions to create points as relative position of ViewPort
    def glVertexRGBRelative(self,x,y,r,g,b):
        xAbs =round(((x+1)*(self.viewPortWidth/2))+ self.viewPortX)
        yAbs =round(((y+1)*(self.viewPortHeight/2))+ self.viewPortY)
        self.pixels[yAbs][xAbs]=colorScale(r,g,b)

    def glVertexColorRelative(self,x,y,color=None):
        try:
            xAbs =round(((x+1)*(self.viewPortWidth/2))+ self.viewPortX)
            yAbs =round(((y+1)*(self.viewPortHeight/2))+ self.viewPortY)
            self.pixels[yAbs][xAbs]=self.currentColor if color == None else color
        except:
            #If tries to draw outside scren
            pass

    #Change current vertex color
    def glColor(self,color):
        self.currentColor=color;

    def glColorRGB(self,r,g,b):
        self.currentColor=colorScale(r,g,b)
    
    #Function to write image in file
    def glFinish(self,filename):
        file = open(filename,'wb')
        #https://itnext.io/bits-to-bitmaps-a-simple-walkthrough-of-bmp-image-format-765dc6857393
        #Reference to construct BMP

        #File Type Data BMP Header 14 Bytes
        file.write(char('B'))
        file.write(char('M'))
        file.write(dword(14+40+self.width*self.height*3))
        file.write(dword(0))
        file.write(dword(14+40))

        #File Image Header 40 Bytes
        file.write(dword(40))
        file.write(dword(self.width))
        file.write(dword(self.height))
        file.write(word(1))
        file.write(word(24))
        file.write(dword(0))
        file.write(dword(self.width*self.height*3))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))

        #Pixels 3 Bytes each
        for x in range(self.height):
            for y in range(self.width):
                 file.write(self.pixels[x][y])
        file.close()

    #Function to write zBuffer in file
    def glFinishZbuffer(self,filename):
        file = open(filename,'wb')
        #https://itnext.io/bits-to-bitmaps-a-simple-walkthrough-of-bmp-image-format-765dc6857393
        #Reference to construct BMP

        #File Type Data BMP Header 14 Bytes
        file.write(char('B'))
        file.write(char('M'))
        file.write(dword(14+40+self.width*self.height*3))
        file.write(dword(0))
        file.write(dword(14+40))

        #File Image Header 40 Bytes
        file.write(dword(40))
        file.write(dword(self.width))
        file.write(dword(self.height))
        file.write(word(1))
        file.write(word(24))
        file.write(dword(0))
        file.write(dword(self.width*self.height*3))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))


        #We first calculate the min and the max depth in z in order to then write on the file
        minZ=0
        maxZ=0
        for x in range(self.height):
            for y in range(self.width):
                depth =self.zbuffer[x][y]
                if(depth!=-float('inf')):
                    minZ= minZ if minZ<depth else depth
                    maxZ= maxZ if maxZ>depth else depth

        #Pixels 3 Bytes each
        for x in range(self.height):
            for y in range(self.width):
                depth=self.zbuffer[x][y]
                depth= depth if depth!=-float('inf') else minZ
                #We normalize depth into a value from 0 to 1.
                intensity=(depth-minZ)/(maxZ-minZ)
                file.write(colorScale(intensity,intensity,intensity))
        file.close()

    #Function for a line
    def glLine(self,x0,y0,x1,y1,color=None):
        #Convert to absolute coordinates
        x0Abs =round(((x0+1)*(self.viewPortWidth/2))+ self.viewPortX)
        y0Abs =round(((y0+1)*(self.viewPortHeight/2))+ self.viewPortY)
        x1Abs =round(((x1+1)*(self.viewPortWidth/2))+ self.viewPortX)
        y1Abs =round(((y1+1)*(self.viewPortHeight/2))+ self.viewPortY)
        dy=y1Abs-y0Abs
        dx=x1Abs-x0Abs
        #Graphic a point if is the same
        if(x0Abs==x1Abs and y0Abs==y1Abs):
             self.glVertexColorAbsolute(round(x0Abs),round(y0Abs))
        
        #If vertical line
        if(dx==0):
            #Vertical Line
            step= +1 if (y1Abs>y0Abs) else -1;
            
            for y in range(y0Abs,y1Abs,step):
                x=x0Abs
                self.glVertexColorAbsolute(round(x),round(y))
        #Any other line
        else:
           #Use mx+b=y if m<=1 else my+b=x m>1
           #This is better for points by set rather tan using just mx+b=y
            m=dy/dx
            if(abs(m)<=1 or dy==0):
                b=y0Abs-(m*x0Abs)
                step = 1 if (dx>0) else -1
                if(m>0 and dy<=0 and dx<=0):
                    step=-1
                elif(m>0 and dy>=0 and dx>=0):
                    step=+1
                
                for x in range(x0Abs,x1Abs,step):
                    y=m*x+b
                    self.glVertexColorAbsolute(round(x),round(y))
            else:
                m=dx/dy
                b=x0Abs-(m*y0Abs)
                step = 1 if (dy>0) else -1
                if(m>0 and dy<=0 and dx<=0):
                    step=-1
                elif(m>0 and dy>=0 and dx>=0):
                    step=+1
                
                for y in range(y0Abs,y1Abs,step):
                    x=m*y+b
                    self.glVertexColorAbsolute(round(x),round(y))
            
            
    #Function for a line Coordenadas absolutas
    def glLineAbsolute(self,x0Abs,y0Abs,x1Abs,y1Abs,color=None):
        if(x0Abs>self.width or y0Abs>self.height or x1Abs>self.width or y1Abs>self.height):
            return False
        dy=y1Abs-y0Abs
        dx=x1Abs-x0Abs
        #Graphic a point if is the same
        if(x0Abs==x1Abs and y0Abs==y1Abs):
             self.glVertexColorAbsolute(round(x0Abs),round(y0Abs))
        
        #If vertical line
        if(dx==0):
            #Vertical Line
            step= +1 if (y1Abs>y0Abs) else -1;
            
            for y in range(y0Abs,y1Abs,step):
                x=x0Abs
                self.glVertexColorAbsolute(round(x),round(y))
        #Any other line
        else:
           #Use mx+b=y if m<=1 else my+b=x m>1
           #This is better for points by set rather tan using just mx+b=y
            m=dy/dx
            if(abs(m)<=1 or dy==0):
                b=y0Abs-(m*x0Abs)
                step = 1 if (dx>0) else -1
                if(m>0 and dy<=0 and dx<=0):
                    step=-1
                elif(m>0 and dy>=0 and dx>=0):
                    step=+1
                
                for x in range(x0Abs,x1Abs,step):
                    y=m*x+b
                    self.glVertexColorAbsolute(round(x),round(y))
            else:
                m=dx/dy
                b=x0Abs-(m*y0Abs)
                step = 1 if (dy>0) else -1
                if(m>0 and dy<=0 and dx<=0):
                    step=-1
                elif(m>0 and dy>=0 and dx>=0):
                    step=+1
                
                for y in range(y0Abs,y1Abs,step):
                    x=m*y+b
                    self.glVertexColorAbsolute(round(x),round(y))
                    
    #Function to render an object with ray tracing
    def rtRender(self):
        #We check for ray in each pixel of our scene
        for y in range(self.height):
            for x in range(self.width):

                # Tranform coordinates from [0,1] to [-1,1]. We also add +0.5 to be in the middle of the pixel
                pX = 2 * ( (x+0.5) / self.width) - 1
                pY = 2 * ( (y+0.5) / self.height) - 1

                #FOV vision angle with camera 1 point away
                top = tan( self.mathGl.degreesToRadians(self.FOV)/2)
                right = top * self.width / self.height
                pX *= right
                pY *= top

                #Camara Direction
                direction = [pX, pY, -1]
                direction = self.mathGl.normalizeVector(direction)
                
                colorRay = self.castRay(self.camPosition,direction)
                if colorRay is not None:
                    self.glVertexColorAbsolute(x, y, color=colorRay)
    
    # Check if there is obj intersect with another
    def sceneIntersect(self,orig,direction,origObj=None):
        material = None
        intersect =None
        hit=None
        tempZBuffer = float('inf')
        #We check for each object in our scene
        for obj in self.sceneObjects:
            if obj is not origObj:
                #We check for intersection with ray and zBuffer to take in account depth
                intersect = obj.ray_intersect(orig, direction)
                if intersect is not None:
                    if intersect.distance < tempZBuffer:
                        tempZBuffer = intersect.distance
                        material = obj.material
                        hit =intersect
        
        return material,hit        
        
    def reflectVector(self,normal,dirVector):
        # reflectLigthDirection = 2 * (normal dot lightDirection) * normal - lightDirection
        reflectLigthDirection = 2 * self.mathGl.dotProductVector(normal, dirVector)
        reflectLigthDirection = self.mathGl.scalarMultiplicationVector(normal,reflectLigthDirection)
        reflectLigthDirection = self.mathGl.subtractVector(reflectLigthDirection, dirVector)
        return reflectLigthDirection

    #To point a color with material and ray intersect
    def castRay(self,orig,direction,origObj=None,recursion=0):
        material,intersect=self.sceneIntersect(orig,direction,origObj)
        if recursion>=maxRecursionDepth or material is None:
            return self.backgroundColor   
        if material is not None:
            objectColor = [material.diffuse[2] / 255,
                        material.diffuse[1] / 255,
                        material.diffuse[0] / 255]
            ambientColor = [0,0,0]
            diffuseColor = [0,0,0]
            specColor = [0,0,0]
            shadowIntensity = 0


            #Get ambienteColor from light
            if self.ambientLight:
                ambientColor =  [self.ambientLight.strength * self.ambientLight.color[2] / 255,
                                self.ambientLight.strength * self.ambientLight.color[1] / 255,
                                self.ambientLight.strength * self.ambientLight.color[0] / 255]

            #Get colors from pointLight
            if self.pointLight:
                # Get light direction of pointLight to calculate intensity
                lightDirection = self.mathGl.subtractVector(self.pointLight.position,intersect.point)
                lightDirection = self.mathGl.normalizeVector(lightDirection)
                intensity = self.mathGl.dotProductVector(lightDirection,intersect.normal)
                intensity = self.pointLight.intensity * max(0,intensity)
                # Calculate actual color of object with light
                diffuseColor = [intensity * self.pointLight.color[2] / 255,
                            intensity * self.pointLight.color[1] / 255,
                            intensity * self.pointLight.color[2] / 255]
                
                # Use specularity
                # We need view direction and light direction of reflection
                viewDirection = self.mathGl.subtractVector(self.camPosition,intersect.point)
                viewDirection = self.mathGl.normalizeVector(viewDirection)
                reflectLigthDirection = self.reflectVector(intersect.normal,lightDirection)
                # spec_intensity: lightIntensity * ( viewDirection dot reflectLigthDirection) ** speculatiry
                specFactor=(max(0, self.mathGl.dotProductVector(viewDirection, reflectLigthDirection)) ** material.specularity)
                specIntensity = self.pointLight.intensity * specFactor
                specColor = [specIntensity * self.pointLight.color[2] / 255,
                        specIntensity * self.pointLight.color[1] / 255,
                        specIntensity * self.pointLight.color[0] / 255]

                #We check each object in our scene for all shadows
                for obj in self.sceneObjects:
                    if obj is not intersect.sceneObject:
                        hit = obj.ray_intersect(intersect.point,  lightDirection)
                        if hit is not None and intersect.distance < self.mathGl.magnitudeVector(self.mathGl.subtractVector(self.pointLight.position, intersect.point)):
                            shadowIntensity = 1
            
            finalColor = None
            #If Material is OPAQUE
            if material.matType==OPAQUE:
                # Calculate final color 
                # (ambientColor + (1 - shadowIntensity) *(specColor + diffuseColor)) * objectColor     
                finalColor = self.mathGl.sumVector(diffuseColor,specColor)
                finalColor = self.mathGl.scalarMultiplicationVector(finalColor,(1-shadowIntensity))
                finalColor =self.mathGl.sumVector(finalColor,ambientColor)
            #If Material is REFLECTIVE
            elif material.matType==REFLECTIVE:
                reflect = self.reflectVector(intersect.normal,viewDirection)
                reflectColor = self.castRay(intersect.point,reflect,intersect.sceneObject,recursion+1)
                reflectColor=[reflectColor[2] / 255,
                        reflectColor[1] / 255,
                        reflectColor[0] / 255]
                finalColor = self.mathGl.scalarMultiplicationVector(specColor,(1-shadowIntensity))
                finalColor =self.mathGl.sumVector(reflectColor,finalColor)
            elif material.matType==TRANSPARENT:
                print("TRANSPARENT")

            finalColor=self.mathGl.multiplyVector(finalColor,objectColor)
            r=min(1,finalColor[0])
            g=min(1,finalColor[1])
            b=min(1,finalColor[2])

            return colorScale(r,g,b)
        return None

    
                    

                