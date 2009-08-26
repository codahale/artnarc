from math import cos, sin, pi
from random import Random
from opencv.cv import *
from opencv.highgui import *
from artnarc.input import Webcam
from artnarc.features import FeatureDetector
from artnarc.util import Point

class GooglyEyes(Webcam):    
    def __init__(self, cascade_filename):
        super(GooglyEyes, self).__init__(window_name="Googly Eyes")
        self.detector = FeatureDetector(cascade_filename)
        self.eye_ratio = 0.15
        self.pupil_ratio = 0.05
        self.fill_color = CV_RGB(255, 255, 255)
        self.color = CV_RGB(0, 0, 0)
        self.thickness = 4
        self.pupils = {"left": 0.0, "right": 0.0}
        self.prng = Random()
    
    def process_frame(self, frame):
        faces = self.detector.detect(frame)
        for f in faces:
            eyeline = int(f.upper_left.y + (0.4 * f.height)) 
            left_eye = int(f.upper_left.x + (0.33 * f.width))
            right_eye = int(f.lower_right.x - (0.33 * f.width))
            self.draw_eyes(frame, eyeline, left_eye, right_eye, f.height)
        cvShowImage(self.window_name, frame)
    
    def draw_eyes(self, frame, eyeline, left_eye_x, right_eye_x, height):
        left_eye = Point(left_eye_x, eyeline)
        right_eye = Point(right_eye_x, eyeline)
        self.draw_eye(frame, left_eye, "left", height)
        self.draw_eye(frame, right_eye, "right", height)
    
    def draw_eye(self, frame, center, tag, height):
        eye_size = int(self.eye_ratio * height)
        cvCircle(frame, center.to_cvPoint(), eye_size, self.fill_color, CV_FILLED, CV_AA)
        cvCircle(frame, center.to_cvPoint(), eye_size, self.color, self.thickness, CV_AA)
        self.draw_pupil(frame, center, tag, height, eye_size)
    
    def draw_pupil(self, frame, center, tag, height, eye_size):
        self.pupils[tag] = (self.pupils[tag] + (self.prng.choice((-2, 1)) * (pi / 10.0))) % (2 * pi)
        inner_eye_size = eye_size * 0.8
        googly_x = center.x + int(inner_eye_size * cos(self.pupils[tag]))
        googly_y = center.y + int(inner_eye_size * sin(self.pupils[tag]))
        pupil_size = int(self.pupil_ratio * height)
        cvCircle(frame, cvPoint(googly_x, googly_y), pupil_size, self.color, CV_FILLED, CV_AA)

if __name__ == "__main__":
    webcam = GooglyEyes("/opt/local/share/opencv/haarcascades/haarcascade_frontalface_alt.xml")
    webcam.run()
