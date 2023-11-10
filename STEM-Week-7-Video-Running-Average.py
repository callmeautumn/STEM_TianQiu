import cv2
from Animator import Animator
import numpy as np

an = Animator()

class MySketch:

    camera = cv2.VideoCapture(0)
    threshold = 50
    window_size = 50
    success, model = camera.read()

    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
        self.camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
        self.model = cv2.resize(self.model,(an.width, an.height))
        self.model = cv2.cvtColor(self.model, cv2.COLOR_BGR2GRAY)
    
    def draw(self):
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed,(an.width, an.height))
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2GRAY)
            
            #Diff against the model
            diff = cv2.absdiff(camera_feed, self.model)
            thresholded = cv2.threshold(diff, self.threshold, 255, cv2.THRESH_BINARY)[1]
            
             #Subtract some percentage of the existing model
            self.model -= self.model // self.window_size
            #Add in some percentage of the new frame
            self.model += camera_feed // self.window_size

            an.canvas = thresholded
        
MySketch()          







