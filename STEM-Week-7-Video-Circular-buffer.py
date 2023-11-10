import cv2
from Animator import Animator
import numpy as np

an = Animator()

class MySketch:

    camera = cv2.VideoCapture(0)
    threshold = 50
    #How big is the buffer?
    window_size = 50
    #Make empty buffer
    buffer = np.zeros((window_size, an.height, an.width)).astype(dtype=np.uint8)
    #Make variable to hold model (avg of buffers)
    model = buffer[0]
    #Where are we in the buffer (write pointer)
    ptr = 0

    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
    
    def draw(self):
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed,(an.width, an.height))
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2GRAY)
            
            diff = cv2.absdiff(camera_feed, self.model)
            thresholded = cv2.threshold(diff, self.threshold, 255, cv2.THRESH_BINARY)[1]
            
            #Update mask with mean pixel values from buffer (axis 0 is time!)
            self.model = np.mean(self.buffer, axis=0).astype(dtype=np.uint8)
            
            #Update the circular buffer
            self.ptr = (self.ptr + 1) % self.window_size
            self.buffer[self.ptr] = camera_feed

            an.canvas = thresholded
        
MySketch()          







