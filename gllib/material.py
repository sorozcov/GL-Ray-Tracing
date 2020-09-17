# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 04/09/2020
#  material.py


# Color function ro return rgb in bytes
def colorScale(r,g,b):
    return bytes([round(b*255),round(g*255),round(r*255)])

# Material with a set of properties for the object and it's interaction with light
class Material(object):

    def __init__(self, diffuse = colorScale(1,1,1),specularity=0):
        # Diffuse Material Color
        self.diffuse = diffuse
        # Specularity to know how reflective a surface is
        # It depends from the point of view
        self.specularity = specularity
        
