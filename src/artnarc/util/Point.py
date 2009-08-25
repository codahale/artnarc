from opencv.cv import cvPoint

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)
    
    def to_cvPoint(self):
        return cvPoint(self.x, self.y)