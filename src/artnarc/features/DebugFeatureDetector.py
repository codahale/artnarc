from opencv.cv import *
from opencv.highgui import *
from FeatureDetector import FeatureDetector

"""
Same thing as FeatureDetector, but with a debug display.
"""
class DebugFeatureDetector(FeatureDetector):
    def __init__(self, cascade_filename):
        super(DebugFeatureDetector, self).__init__(cascade_filename)
        cvNamedWindow("Features")
    
    def detect(self, frame):
        features = super(DebugFeatureDetector, self).detect(frame)
        for f in features:
            cvRectangle(self.frame_copy, f.upper_left.to_cvPoint(), f.lower_right.to_cvPoint(), CV_RGB(255,0,0), 3, 8, 0)
        cvShowImage("Features", self.frame_copy)
        return features