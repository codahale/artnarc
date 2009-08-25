from opencv.cv import *
from opencv.highgui import *
from artnarc.features import Feature

"""
A feature detector. Uses Haar classifier cascades.
"""
class FeatureDetector(object):
    def __init__(self, cascade_filename):
        self.cascade = cvLoadHaarClassifierCascade(cascade_filename, cvSize(1, 1))
        self.storage = cvCreateMemStorage(0)
        self.min_size = cvSize(20,20)
        self.image_scale = 1.3
        self.haar_scale = 1.2
        self.min_neighbors = 2
        self.haar_flags = CV_HAAR_DO_CANNY_PRUNING
        self.frame_copy = None
    
    def detect(self, frame):
        self.copy_frame(frame)
        small_img = self.resize_frame(self.frame_copy)
        features = cvHaarDetectObjects(small_img, self.cascade, self.storage, self.haar_scale, self.min_neighbors, self.haar_flags, self.min_size)
        return [Feature(f, self.image_scale) for f in features]
    
    def copy_frame(self, frame):
        if not self.frame_copy:
            self.frame_copy = cvCreateImage(cvSize(frame.width,frame.height), IPL_DEPTH_8U, frame.nChannels)
        if frame.origin == IPL_ORIGIN_TL:
            cvCopy(frame, self.frame_copy)
        else:
            cvFlip(frame, self.frame_copy)
    
    def resize_frame(self, frame_copy):
        gray = cvCreateImage(cvSize(self.frame_copy.width, self.frame_copy.height), 8, 1)
        small_img = cvCreateImage(cvSize(cvRound(self.frame_copy.width / self.image_scale), cvRound(self.frame_copy.height / self.image_scale)), 8, 1)
        cvCvtColor(self.frame_copy, gray, CV_BGR2GRAY)
        cvResize(gray, small_img, CV_INTER_LINEAR)
        cvEqualizeHist(small_img, small_img)
        cvClearMemStorage(self.storage)
        return small_img
