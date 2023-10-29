import numpy as np
from cv2 import line
from Animator import Animator
from MusicAnalyser import MusicAnalyser

file_path = "audio/gospel.wav"
mus = MusicAnalyser(file_path)
an = Animator(640,480)

class MySketch:

    def __init__(self):
        an.start_loop(self.setup, self.draw)  
            
    def setup(self):
        print("setup")
        
    def draw(self):
        an.background(0)
        for i,val in enumerate(mus.fft_vals):
            x = i*2
            y = an.height-int(val*100)
            line(an.canvas, (x, an.height), (x,y), (0,255,0), 1)
            

MySketch()