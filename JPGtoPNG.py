import os
from tkinter import Image 
from PIL import Image

def converter(nev):
    img = Image.open(f'./{nev}.jpg')
    img.show()
    img.save(f'{nev}.png')

 #a kuurva széfta tiszpfha neg
converter('bulbasaur')


#for root,dir,files in os.walk('/home/lovaszimarci/Pokedex'):
 #   for file in files:
  #      if 'jpg' in files:


