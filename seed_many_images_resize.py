import cv2
from Animator import Animator
from mosaic import get_images
import numpy as np
from PIL import Image

an = Animator(300,300)

class MySketch:

    thumbnail_size = (an.width,an.height)
    dataset = get_images("data/animal_thumbnails/land_mammals", thumbnail_size)
    current_image = 0

    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        return

    def draw(self):
        
        new_canvas = Image.new('RGB', (an.width, an.height))
        to_paste = self.dataset[self.current_image]
        to_paste = Image.fromarray(to_paste)
        
        #Use the sin function (goes between -1 and 1) and an.frame to oscillate big and small
        w = int(np.abs(np.sin(an.frame/30))*an.width//2)+1
        h = int(np.abs(np.sin(an.frame/30))*an.height//2)+1

        #Change image whenever the image gets small
        if w < 10:
            self.current_image = np.random.randint(len(self.dataset))

        to_paste = to_paste.resize((w, h))
        #Also change where we paste based on w and h
        coords = (w//2,h//2)
        #Paste into canvas
        new_canvas.paste(to_paste, coords)
        an.canvas = np.array(new_canvas)

MySketch()          







