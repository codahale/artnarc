class Rect(object):
    def __init__(self, upper_left, lower_right):
        self.upper_left = upper_left
        self.lower_right = lower_right
        self.width = lower_right.x - upper_left.x
        self.height = lower_right.y - upper_left.y 
    
    def __repr__(self):
        return "Rect(%s, %s)" % (self.upper_left, self.lower_right) 