from opencv.cv import *
from opencv.highgui import *

"""
A basic read-crap-from-webcam-and-display-it kind of thing.

Y'know.
"""
class Webcam(object):
    def __init__(self, window_name = "Input", camera_index = 0):
        self.camera = cvCreateCameraCapture(camera_index)
        self.window_name = window_name
        cvNamedWindow(window_name, CV_WINDOW_AUTOSIZE);
    
    """
    Do a damn thing.
    """
    def run(self):
        while True:
            frame = cvQueryFrame(self.camera)
            self.process_frame(frame)
            if cvWaitKey(10) >= 0:
                break
        cvDestroyWindow(self.window_name);
    
    """
    Make this do the thing you want it to do.
    """
    def process_frame(self, frame):
        cvShowImage(self.window_name, frame)