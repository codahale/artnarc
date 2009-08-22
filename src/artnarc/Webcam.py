from opencv.cv import *
from opencv.highgui import *

class Webcam(object):
    def __init__(self, window_name = "Input", camera_index = 0):
        self.camera = cvCreateCameraCapture(camera_index)
        self.window_name = window_name
        cvNamedWindow(window_name, CV_WINDOW_AUTOSIZE);
    
    def run(self):
        while True:
            frame = cvQueryFrame(self.camera)
            self.process_frame(frame)
            if cvWaitKey(10) >= 0:
                break
        cvDestroyWindow(self.window_name);
    
    def process_frame(self, frame):
        cvShowImage(self.window_name, frame)