import cv2
from Animator import Animator

an = Animator()

class MySketch:
    
    #Set up camera
    camera = cv2.VideoCapture(0)

    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
        #Turn off autofocus
        self.camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    
    def draw(self):
        #Pull in frame
        success, camera_feed = self.camera.read()
        if success:
            #Convert color
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2RGB)
            #Resize to canvas size
            camera_feed = cv2.resize(camera_feed,(an.width, an.height))
            #Write to screen
            an.canvas = camera_feed
        
MySketch()          







