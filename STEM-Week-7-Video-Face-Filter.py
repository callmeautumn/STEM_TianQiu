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
            ##ADD YOUR OWN CODE IN HERE
                # Draw sunglasses shape (here, a rectangle for demonstration purposes)
                glass_width = int(face_w * 0.6)
                glass_height = int(face_h * 0.15)
                glass_x = face_x + int((face_w - glass_width) / 2)
                glass_y = face_y + int(face_h * 0.35)
                
                # Draw the frame of the sunglasses (curved shape)
                cv2.ellipse(camera_feed, (face_x + face_w // 2, glass_y + glass_height // 2), 
                            (glass_width // 2, glass_height // 2), 0, 0, 180, (0, 0, 0), -1)
                
                # Draw the left lens of the sunglasses (ellipse)
                cv2.ellipse(camera_feed, (glass_x + int(glass_width * 0.25), glass_y + glass_height // 2), 
                            (int(glass_width * 0.2), int(glass_height * 0.8)), 0, 0, 360, (0, 0, 0), -1)
                
                # Draw the right lens of the sunglasses (ellipse)
                cv2.ellipse(camera_feed, (glass_x + int(glass_width * 0.75), glass_y + glass_height // 2), 
                            (int(glass_width * 0.2), int(glass_height * 0.8)), 0, 0, 360, (0, 0, 0), -1)
        
MySketch()          







