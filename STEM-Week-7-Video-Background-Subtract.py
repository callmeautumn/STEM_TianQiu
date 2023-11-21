

import cv2
from Animator import Animator

an = Animator()

class MySketch:

    camera = cv2.VideoCapture(0)
    #Save first frame as background
    success, camera_background = camera.read()

    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
        self.camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
        self.camera_background = cv2.resize(self.camera_background,(an.width, an.height))
        self.camera_background = cv2.cvtColor(self.camera_background, cv2.COLOR_BGR2GRAY)
    
    def draw(self):
        an.background((255,255,255))
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed,(an.width, an.height))
            camera_feed= cv2.cvtColor(camera_feed, cv2.COLOR_BGR2GRAY)
            #Absolute difference between current frame and first frame (background)
            diff = cv2.absdiff(camera_feed, self.camera_background)
            an.canvas = diff
        
MySketch()          







