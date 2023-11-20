from Animator import Animator
from MusicAnalyser import MusicAnalyser
from skimage import measure
import numpy as np
import cv2
import matplotlib.pyplot as plt

an = Animator(1500,1500)
file_path = "audio/noise.wav"
mus = MusicAnalyser(file_path)

class MySketch:

    image = []
    bbox = []
    directions = []
    ptr = 0

    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        fp = "/Users/louisbusby/Documents/UAL/23-24/STEM/STEM-4-Creatives-23-24/images/portraits/mahmoud-saiid_16.jpg"
        #fp = "/Users/louisbusby/Documents/UAL/23-24/STEM/STEM-4-Creatives-23-24/images/portraits/nikolay-bogdanov-belsky_40.jpg"
        #fp = "/Users/louisbusby/Downloads/IMG_4016.jpg"
        self.image = cv2.imread(fp)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.im_w = self.image.shape[1]
        self.im_h = self.image.shape[0]
        self.gray_example = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        _, self.thresh= cv2.threshold(self.gray_example, 100, 255, cv2.THRESH_BINARY)
        #Get contours 
        level = 0.3
        self.contours = measure.find_contours(self.thresh, level)
        self.contours = [np.array(c[:, [1, 0]], dtype=np.int32) for c in self.contours if len(c)>3]
        #Filter contours 
        new_list = []
        #Only keep closed
        # self.contours= [c for c in self.contours if c[0,1] == c[-1,1] and c[0,0] == c[-1,0]]
        for c in self.contours:
            if not (c[0,1] == c[-1,1] and c[0,0] == c[-1,0]):
                c[-1] = c[0]
        self.topk = 150
        self.areas = np.array([cv2.contourArea(contour) for contour in self.contours])
        #Keep top k biggest contours (by area)
        indexes = self.areas.argsort()[-self.topk:]
        areas = []
        for i in indexes:
            if self.areas[i]>10:
                contour = self.contours[i]
                new_list.append(contour)
                areas.append(self.areas[i])
                self.bbox.append(cv2.boundingRect(contour))
                self.directions.append([np.random.choice([-1,0,1]),np.random.choice([-1,0,1])])
        self.contours = new_list
        self.areas = areas
        print("Contours:", len(self.contours))
        self.top_y = (an.height-self.im_h)//2
        self.top_x = (an.width-self.im_w)//2
        self.offset = np.pi
        #an.canvas[self.top_y:self.top_y+self.im_h,self.top_x:self.top_x+self.im_w] = self.image
        an.background((0,0,0))
    def draw(self):
        #an.background((255,255,255))
        #an.canvas[self.top_y:self.top_y+self.im_h,self.top_x:self.top_x+self.im_w] = self.image
        
        self.ptr+=5
        new_canvas = an.to_alpha(0.2)
        for index, contour in enumerate(self.contours):
            #cut out the shape
            mask = np.zeros(self.image.shape[:2], dtype=np.uint8)
            cv2.drawContours(mask, [contour], -1, (255), thickness=cv2.FILLED)
            cut_out = cv2.bitwise_and(self.image, self.image, mask=mask)
            #cv2.drawContours(new_canvas, [contour], -1, self.c(index/35), thickness=cv2.FILLED)
            x,y,w,h = self.bbox[index]
            cut_out = cut_out[y:y+h,x:x+w]

            #theta = (np.pi*2) * (mus.fft_vals[index]*20)
            theta = (np.pi*2) * (index/len(self.contours))
            if np.random.random()<0.0005:
                self.offset = np.random.choice([0,np.pi/4,np.pi/2,np.pi*0.75, np.pi, np.pi*1.25, np.pi*1.5, np.pi*1.75])
            
            theta += self.offset
            delta_y = np.abs((y + self.top_y) - an.height//2)
            delta_x = np.abs((x + self.top_x) - an.width//2)
            r = np.sqrt((delta_x**2 + delta_y**2)) 
            r = (r * (mus.fft_vals[index]/6))
            #r = an.width // 3
            new_y = int((y + self.top_y) + ((r)*np.cos(theta)))
            new_x = int((x + self.top_x) + ((r)*np.sin(theta)))
            #Only draw if inside boundary of canvas
            if new_y+h<an.height and new_y>=0 and new_x+w<an.width and new_x>=0:
                #Draw to contour layer
                new_canvas[new_y:new_y + h, new_x:new_x + w] = cut_out
        
        #Overlay contours back onto main canvas
        # an.pop_layer(new_canvas)

MySketch()          
