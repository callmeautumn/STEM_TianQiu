import cv2
from Animator import Animator

an = Animator()

class MySketch:

    camera = cv2.VideoCapture(0)
    success, camera_background = camera.read()
    threshold = 50

    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        self.camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
        self.camera_background = cv2.resize(self.camera_background,(an.width, an.height))
    
    def draw(self):
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed,(an.width, an.height))
            diff = cv2.absdiff(camera_feed, self.camera_background)
            diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            #Threshhold the difference (make binary)
            thresholded = cv2.threshold(diff, self.threshold, 255, cv2.THRESH_BINARY)[1]
            an.canvas = thresholded
        
MySketch()          







