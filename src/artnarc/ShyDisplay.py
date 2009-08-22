#!/usr/bin/python

from opencv.cv import *
from opencv.highgui import *
from artnarc import Webcam

"""
A webcam display which gets shy when you look at it.
"""
class ShyDisplay(Webcam):
    max_face_samples = 3
    min_face_count = 1
    min_size = cvSize(20,20)
    image_scale = 1.3
    haar_scale = 1.2
    min_neighbors = 2
    haar_flags = CV_HAAR_DO_CANNY_PRUNING
    
    def __init__(self, cascade_filename):
        super(ShyDisplay, self).__init__()
        self.face_count = []
        self.cascade = cvLoadHaarClassifierCascade(cascade_filename, cvSize(1,1));
        self.storage = cvCreateMemStorage(0)
        self.frame_copy = None
    
    def process_frame(self, frame):
        if not self.frame_copy:
            self.frame_copy = cvCreateImage(cvSize(frame.width,frame.height), IPL_DEPTH_8U, frame.nChannels);
        if frame.origin == IPL_ORIGIN_TL:
            cvCopy(frame, self.frame_copy);
        else:
            cvFlip(frame, self.frame_copy);
        
        gray = cvCreateImage(cvSize(self.frame_copy.width, self.frame_copy.height), 8, 1)
        small_img = cvCreateImage(
                                  cvSize(cvRound (self.frame_copy.width / self.image_scale),
                                         cvRound(self.frame_copy.height / self.image_scale)
                                         ),
                                  8, 1)
        cvCvtColor(self.frame_copy, gray, CV_BGR2GRAY)
        cvResize(gray, small_img, CV_INTER_LINEAR)
        cvEqualizeHist(small_img, small_img)
        cvClearMemStorage(self.storage);
        
        faces = cvHaarDetectObjects(small_img, self.cascade, self.storage,
                                     self.haar_scale, self.min_neighbors, self.haar_flags, self.min_size);
        if faces:
            self.adjust_face_count(faces.total)
        if self.has_faces():
            cvSetZero(self.frame_copy)
        cvShowImage(self.window_name, self.frame_copy)
    
    def adjust_face_count(self, count):
        self.face_count = [count] + self.face_count[0:self.max_face_samples - 1]
    
    def has_faces(self):
        print self.face_count
        return sum(self.face_count) >= self.min_face_count
        

if __name__ == "__main__":
    webcam = ShyDisplay("/opt/local/share/opencv/haarcascades/haarcascade_frontalface_alt.xml")
    webcam.run()
