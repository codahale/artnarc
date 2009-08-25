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
        if features:
            for r in features:
                pt1 = cvPoint(int(r.x*self.image_scale), int(r.y*self.image_scale))
                pt2 = cvPoint(int((r.x+r.width)*self.image_scale), int((r.y+r.height)*self.image_scale))
                cvRectangle(self.frame_copy, pt1, pt2, CV_RGB(255,0,0), 3, 8, 0)
        cvShowImage("Features", self.frame_copy)
        return features