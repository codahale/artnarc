from opencv.cv import *
from opencv.highgui import *
from Webcam import Webcam
from FeatureDetector import FeatureDetector

"""
A webcam display which gets shy when you look at it.
"""
class ShyDisplay(Webcam):
    max_face_samples = 3
    min_face_count = 1
    
    def __init__(self, cascade_filename):
        super(ShyDisplay, self).__init__()
        self.face_count = []
        self.detector = FeatureDetector(cascade_filename)
    
    def process_frame(self, frame):
        faces = self.detector.detect(frame)
        if faces:
            self.face_count = [faces.total] + self.face_count[0:self.max_face_samples - 1]
        if sum(self.face_count) >= self.min_face_count:
            cvSetZero(frame)
        cvShowImage(self.window_name, frame)
        

if __name__ == "__main__":
    webcam = ShyDisplay("/opt/local/share/opencv/haarcascades/haarcascade_frontalface_alt.xml")
    webcam.run()
