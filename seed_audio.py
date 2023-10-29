import numpy as np
from cv2 import circle
from Animator import Animator
from MusicAnalyser import MusicAnalyser

file_path = "audio/gospel.wav"
mus = MusicAnalyser(file_path)
an = Animator(640,480)

class MySketch:

    def __init__(self):
        an.start_loop(self.setup, self.draw)  
            
    def setup(self):
        wave = []
        window_size = 1024
        num_buffers = len(mus.y)//window_size
        #Do this code to every buffer
        for i in range(num_buffers):
            start = i*window_size
            end = (i+1)*window_size
            buffer = mus.y[start:end]
            mean = np.abs(buffer.mean())
            wave.append(mean)
        for i,b in enumerate(wave):
            #draw a circle based on the mean volume of each buffer
            circle(an.to_alpha(0.2), (i*2,an.height//2), int(b*30000), (255,0,0), -1)
        
    def draw(self):
        return
            

MySketch()