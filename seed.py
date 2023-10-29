from cv2 import rectangle, line, circle, ellipse, polylines
from Animator import Animator

an = Animator()

class MySketch:

    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")

        #These two bits of code are the same!

        #Arguments in place
        rectangle(an.canvas, (0,0), (100,100), (0,0,255), -1)

        #Arguments stored in named variables first
        x1 = 0
        y1 = 0
        x2 = 100
        y2 = 100
        colour = (0,0,255)
        border = -1
        rectangle(an.canvas, (x1,y1), (x2,y2), colour, border)

    def draw(self):
        return

MySketch()          







