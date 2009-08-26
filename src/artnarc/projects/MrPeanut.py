# -*- coding: utf-8 -*-
from math import cos, sin, pi
from random import Random
from opencv.cv import *
from opencv.highgui import *
from artnarc.input import Webcam
from artnarc.features import FeatureDetector
from artnarc.util import Point

class MrPeanut(Webcam):    
    def __init__(self, cascade_filename):
        super(MrPeanut, self).__init__(window_name="Senor Cacahuete")
        self.detector = FeatureDetector(cascade_filename)
        self.eye_ratio = 0.15
        self.pupil_ratio = 0.05
        self.fill_color = CV_RGB(255, 255, 255)
        self.color = CV_RGB(0, 0, 0)
        self.thickness = 4
    
    def process_frame(self, frame):
        faces = self.detector.detect(frame)
        for f in faces:
            eyeline = int(f.upper_left.y + (0.4 * f.height))
            left_eye = cvPoint(int(f.upper_left.x + (0.33 * f.width)), eyeline)
            self.draw_monocle(frame, left_eye, f.height)
            self.draw_hat(frame, f)
        cvShowImage(self.window_name, frame)
    
    def draw_monocle(self, frame, center, height):
        eye_size = int(self.eye_ratio * height)
        cvCircle(frame, center, eye_size, self.fill_color, CV_FILLED, CV_AA)
        cvCircle(frame, center, eye_size, self.color, self.thickness, CV_AA)
    
    def draw_hat(self, frame, rect):
        face_midline = rect.upper_left.x + (rect.width / 2.0)        
        brim_line = rect.upper_left.y - (rect.height * 0.1)
        brim_width = rect.width * 1.4
        brim_height = 40
        hat_width = rect.width * 0.8
        hat_height = 100
        cvRectangle(frame, cvPoint(int(face_midline) - int(brim_width / 2.0), int(brim_line)), cvPoint(int(face_midline) + int(brim_width / 2.0), int(brim_line) + brim_height), self.color, CV_FILLED, CV_AA)
        cvRectangle(frame, cvPoint(int(face_midline) - int(hat_width / 2.0), int(brim_line) - hat_height), cvPoint(int(face_midline) + int(hat_width / 2.0), int(brim_line)), self.color, CV_FILLED, CV_AA)

if __name__ == "__main__":
    webcam = MrPeanut("/opt/local/share/opencv/haarcascades/haarcascade_frontalface_alt.xml")
    webcam.run()
