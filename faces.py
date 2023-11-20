import cv2 as cv2
import numpy as np
from PIL import ImageOps
import PIL

#This task is broadly based on [Data Hackers](http://datahacker.rs/opencv-for-hackers/)

def get_face(img):
    #First find the face
    face_cascade=cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
    #Here is a picture of Kimberly Bryant, founder of Black Girls Code
    
    faces= face_cascade.detectMultiScale(img, 1.1, 4)
    print("faces", len(faces))
    # Defining and drawing the rectangle around the face
    for x, y, w, h in faces[:1]:
        cv2.rectangle(img, (x,y) ,(x+w, y+h), (0,255,0), 3)
    return img,x,y,w,h

def get_eyes(img,x,y,w,h):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    roi_gray = gray[y:(y+h), x:(x+w)]
    roi_color = img[y:(y+h), x:(x+w)]
    # Creating variable eyes
    eye_cascade=cv2.CascadeClassifier("data/haarcascade_eye.xml")
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
    index = 0
    print("eyes", len(eyes))
    if len(eyes)==2 :
        # Creating for loop in order to divide one eye from another
        for (ex , ey,  ew,  eh) in eyes:
            if index == 0:
                #Save the eyes as TUPLES
                eye_1 = (ex, ey, ew, eh)
            elif index == 1:
                eye_2 = (ex, ey, ew, eh)
            # Drawing rectangles around the eyes
            cv2.rectangle(roi_color, (ex,ey) ,(ex+ew, ey+eh), (0,0,255), 1)
            index = index + 1

        if eye_1[0] < eye_2[0]:
            left_eye = eye_1
            right_eye = eye_2
        else:
            left_eye = eye_2
            right_eye = eye_1
        # Calculating coordinates of a central points of the rectangles
        left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
        left_eye_x = left_eye_center[0] 
        left_eye_y = left_eye_center[1]
        
        right_eye_center = (int(right_eye[0] + (right_eye[2]/2)), int(right_eye[1] + (right_eye[3]/2)))
        right_eye_x = right_eye_center[0]
        right_eye_y = right_eye_center[1]
        
        cv2.circle(roi_color, left_eye_center, 2, (255, 0, 0) , 1)
        cv2.circle(roi_color, right_eye_center, 2, (255, 0, 0) , 1)
        cv2.line(roi_color,right_eye_center, left_eye_center,(0,200,200),1)
        if left_eye_y > right_eye_y:
            A = (right_eye_x, left_eye_y)
            # Integer -1 indicates that the image will rotate in the clockwise direction
            direction = -1 
        else:
            A = (left_eye_x, right_eye_y)
            # Integer 1 indicates that image will rotate in the counter clockwise  
            # direction
            direction = 1 
        print(direction)
        cv2.circle(roi_color, A, 5, (255, 0, 0) , -1)
        
        cv2.line(roi_color,right_eye_center, left_eye_center,(0,200,200),1)
        cv2.line(roi_color,left_eye_center, A,(0,200,200),1)
        cv2.line(roi_color,right_eye_center, A,(0,200,200),1)
        return roi_color,left_eye_x,left_eye_y,right_eye_x,right_eye_y
    return roi_color,0,0,1,1

def align_faces(dataset):

    just_faces = []
    original = []
    for i in range(len(dataset)):
        img = dataset[i].copy()
        #First find the face
        face_cascade=cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
        eye_cascade=cv2.CascadeClassifier("data/haarcascade_eye.xml")
        # Converting the image into grayscale
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Creating variable faces
        faces= face_cascade.detectMultiScale(img, 1.1, 4)
        # Defining and drawing the rectangle around the face
        if len(faces)>0:
            fx,fy,fw,fh = faces[0]
            roi_gray=gray[fy:(fy+fh), fx:(fx+fw)]
            # Creating variable eyes
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
            index=0
            if len(eyes)>1:
                # Creating for loop in order to divide one eye from another
                for (ex , ey,  ew,  eh) in eyes:
                    if index == 0:
                        #Save the eyes as TUPLES
                        eye_1 = (ex, ey, ew, eh)
                    elif index == 1:
                        eye_2 = (ex, ey, ew, eh)
                    # Drawing rectangles around the eyes
                    index = index + 1

                if eye_1[0] < eye_2[0]:
                    left_eye = eye_1
                    right_eye = eye_2
                else:
                    left_eye = eye_2
                    right_eye = eye_1
                # Calculating coordinates of a central points of the rectangles
                left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
                left_eye_x = left_eye_center[0] 
                left_eye_y = left_eye_center[1]
                
                right_eye_center = (int(right_eye[0] + (right_eye[2]/2)), int(right_eye[1] + (right_eye[3]/2)))
                right_eye_x = right_eye_center[0]
                right_eye_y = right_eye_center[1]
                adjacent = right_eye_x - left_eye_x
                opposite = right_eye_y - left_eye_y
                if adjacent > 0:
                    angle = np.arctan(opposite/adjacent)
                    angle = (angle * 180) / np.pi
                    h, w = img.shape[:2]
                    center = (int(fx), int(fy))
                    print(center, angle)
                    M = cv2.getRotationMatrix2D(center, (angle), 1.0)
                    rotated = cv2.warpAffine(img, M, (w, h))
                    thumbnail_size = (128,128)
                    cropped = rotated[fy:(fy+fh), fx:(fx+fw)]
                    resized = ImageOps.fit(PIL.Image.fromarray(cropped), thumbnail_size)
                    print("saving!", i)
                    just_faces.append(resized)
                    original.append(ImageOps.fit(PIL.Image.fromarray(img), thumbnail_size))
    return just_faces, original