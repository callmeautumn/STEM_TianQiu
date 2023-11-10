import cv2
from Animator import Animator

an = Animator()

class MySketch:

    face_cascade=cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
    camera = cv2.VideoCapture(0)
    
    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
    
    def draw(self):
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed,(an.width, an.height))
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2RGB)
            camera_feed_grayscale = cv2.cvtColor(camera_feed, cv2.COLOR_RGB2GRAY)
            faces = self.face_cascade.detectMultiScale(camera_feed_grayscale, 1.1, 4)

            for face_x, face_y, face_w, face_h in faces:
            #Draw rectangle around face
            ##ADD YOUR OWN CODE IN HERE
                cv2.circle(camera_feed,
                            (face_x+face_w//2,face_y+face_h//2),
                            face_w//2,255,-1)
            
            an.canvas = camera_feed
        
MySketch()          







