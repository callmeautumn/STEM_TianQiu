import cv2
from Animator import Animator
from mosaic import get_images
import numpy as np
from PIL import Image

an = Animator(800,800)

class MySketch:

    thumbnail_size = (40,40)
    dataset = get_images("data/animal_thumbnails/land_mammals", thumbnail_size)
    number_of_walkers = 100
    images = []
    positions = []

    def __init__(self):
        an.start_loop(self.setup, self.draw)
        

    def setup(self):
        #Get some images and default start positions
        for _ in range(self.number_of_walkers):
            #Add a random image to the list
            self.images.append(np.random.randint(len(self.dataset)))  
            #Add a random start point (x,y) for the image
            self.positions.append([np.random.randint(an.width), np.random.randint(an.height)])
        self.positions = np.array(self.positions)

    def draw(self):

        an.background((255,255,255))
        new_canvas = Image.new('RGB', (an.width, an.height))

        #Iterate through the images
        for index,image in enumerate(self.images):

            to_paste = self.dataset[image]
            to_paste = Image.fromarray(to_paste)

            #Update the position with a random value
            #x
            self.positions[index,0] += np.random.randint(3)
            #y
            self.positions[index,1] += np.random.randint(3)

            #Paste into the the canvas
            coords = tuple(self.positions[index])
            new_canvas.paste(to_paste, coords)

        an.canvas = np.array(new_canvas)

MySketch()          







