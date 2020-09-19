# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 16/09/2020
#  light.py


# Color function ro return rgb in bytes
def colorScale(r,g,b):
    return bytes([round(b*255),round(g*255),round(r*255)])

# Light class object POINT LIGHT
class PointLight(object):
    #Init point light
    def __init__(self, position=(0,0,0),color=colorScale(1,1,1),intensity=1): 
        self.position = position
        self.color = color
        self.intensity = intensity

# Light class object AMBIENT LIGHT SIMULATION
class AmbientLight(object):
    #Init point light
    def __init__(self, color=colorScale(1,1,1),strength=0): 
        self.color = color
        self.strength = strength
