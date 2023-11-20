import cv2
from Animator import Animator
from mosaic import get_images
import numpy as np
from PIL import Image

an = Animator(500,500)

class MySketch:

    thumbnail_size = (100,100)
    #read in images
    dataset = get_images("images/aligned_faces", thumbnail_size)
    #initial random images
    current_images = np.random.randint(0,len(dataset),(5,5))

    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        self.num_rows = self.current_images.shape[0]
        self.num_cols = self.current_images.shape[1]
        return

    def draw(self):
        new_canvas = Image.new('RGB', (an.width, an.height))
        #Iterate through grid and draw images 
        for i in range(self.num_rows):
            for j in range(self.num_cols): 
                to_paste = self.dataset[self.current_images[i,j]]
                #Coordinates of where to paste in images 
                x = i * self.thumbnail_size[0]
                y = j * self.thumbnail_size[1]
                coords = (int(x),int(y))
                new_canvas.paste(Image.fromarray(to_paste), coords)
        
        #if mouse is pressed
        if an.mouse_down:
            #Find which image we are over
            x = an.mouse_x // self.thumbnail_size[0]
            y = an.mouse_y // self.thumbnail_size[1]
            #pick new image
            self.current_images[x,y] = np.random.randint(0,len(self.dataset))
            
        an.canvas = np.array(new_canvas)

MySketch()          







