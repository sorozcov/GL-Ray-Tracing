# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 20/07/2020
# obj.py

import struct
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from gllib.mathgl import MathGl
import numpy as np
from numpy import arccos, arctan2 
#color function ro return rgb in bytes
def colorScale(r,g,b):
    return bytes([round(b*255),round(g*255),round(r*255)])
    
# Class to load a obj file
class Obj(object):
    

   #Initializer, takes as param the filename of obj that is reading
   def __init__(self,filename):
       #Initialize variables needed to store an obj file
       self.fileLines=[]
       self.vertexIndexes = []
       self.vertexTextureIndexes = []
       self.vertexNormalIndexes = []
       self.faces = []
       try:
           #Read file with its lines
           with open(filename,'r') as objFile:
               self.fileLines = objFile.read().splitlines()
               #We parse object to our obj class
               self.parseObject()

       except:
            print("El filename no ha sido encontrado para crear el obj.")
            return

   #Parse obj file properties to my class obj
   def parseObject(self):
        for line in self.fileLines:
            try:
                splitLine = line.split(None,1)
                type= splitLine[0]
                
                values=[]
                if(type[0]=='v'):

                    values=[float(val) for val in splitLine[1].split()]
                else:
                    
                    for f in splitLine[1].split():
                        if(len(f)!=0):
                            values.append([(int(val) if val!='' else 0) for val in f.split("/")])
                            
    
                    
                #You can also do list(map(float, splitLine[1])) parses completely to float
                #Now we save them in our object properties
                
                #Vertex Indexes
               
                if(type=='v'):
                    
                    self.vertexIndexes.append(values)
                #Vertex Normal Indexes    
                elif(type=='vn'):
                    self.vertexNormalIndexes.append(values)
                #Vertex Texture Indexes    
                elif(type=='vt'):
                    self.vertexTextureIndexes.append(values)
                elif(type=='f'):
                     self.faces.append(values)
            except:
                #Manage error if needed but most likely is just a line with another info not needed right now
                pass


# Class to texture 
class Texture(object):
   #Initializer, takes as param the filename of obj that is reading
    def __init__(self, filename):
        self.filename = filename
        self.parseTexture()
    
    #We parse our texture coming from a bmp file    
    def parseTexture(self):
        #Read in bytes
        textureFile = open(self.filename, 'rb')
        textureFile.seek(10)
        headerSize = struct.unpack('=l', textureFile.read(4))[0]

        textureFile.seek(14 + 4)
        self.width = struct.unpack('=l', textureFile.read(4))[0]
        self.height = struct.unpack('=l', textureFile.read(4))[0]
        textureFile.seek(headerSize)

        self.pixels = []

        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(textureFile.read(1)) / 255
                g = ord(textureFile.read(1)) / 255
                r = ord(textureFile.read(1)) / 255
                self.pixels[y].append(colorScale(r,g,b))

        textureFile.close()

    def getColor(self, tx, ty):
        #tx and ty coords should be between 0 and 1
        if tx >= 0 and tx <= 1 and ty >= 0 and ty <= 1:
            #We transform to absolute texture coords
            x = int(tx * self.width)
            y = int(ty * self.height)
            return self.pixels[y][x]
        else:
            #We return black
            return colorScale(0,0,0)

# Class Envmap 
class Envmap(object):
    def __init__(self, filename):
        self.filename = filename
        self.mathGl = MathGl()
        self.parseEnvmap()
        
    def parseEnvmap(self):
        file = open(self.filename, 'rb')
        file.seek(10)
        headerSize = struct.unpack('=l', file.read(4))[0]

        file.seek(14 + 4)
        self.width = struct.unpack('=l', file.read(4))[0]
        self.height = struct.unpack('=l', file.read(4))[0]
        file.seek(headerSize)

        self.pixels = []

        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(file.read(1)) / 255
                g = ord(file.read(1)) / 255
                r = ord(file.read(1)) / 255
                self.pixels[y].append(colorScale(r,g,b))

        file.close()

    def getColor(self, direction):
        direction = self.mathGl.normalizeVector(direction)
        x = int( (arctan2( direction[2], direction[0]) / (2 * np.pi) + 0.5) * self.width)
        y = int( arccos(-direction[1]) / np.pi * self.height )
        # tx=direction[0]
        # ty=direction[1]
        # x = int(tx * self.width)
        # y = int(ty * self.height)
        
        return self.pixels[y][x]