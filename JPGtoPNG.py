import os
from tkinter import Image 
from PIL import Image
from pyparsing import srange

def converter_inside(nev):
    img = Image.open(f'{nev}')
    img.show
    str(img).replace(".jpg","")
    img.save(f'{nev}.png')

 

def converter(): 
    for root,dir,files in os.walk('/home/lovaszimarci/Pokedex'):
        for file in files:
            if ('jpg') in file:
                converter_inside(file)

converter()

