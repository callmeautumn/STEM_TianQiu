import cv2
from Animator import Animator
from mosaic import get_images
import numpy as np
from PIL import Image

an = Animator(300,300)

class MySketch:

    thumbnail_size = (an.width,an.height)
    dataset = get_images("images/aligned_faces", thumbnail_size)
    current_image = 0

    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        return

    def draw(self):
        new_canvas = Image.new('RGB', (an.width, an.height))
        to_paste = self.dataset[np.random.randint(len(self.dataset))]
        coords = (0,0)
        new_canvas.paste(Image.fromarray(to_paste), coords)
        an.canvas = np.array(new_canvas)

MySketch()          







