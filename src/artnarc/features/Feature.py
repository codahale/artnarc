from artnarc.util import Point, Rect

class Feature(Rect):
	def __init__(self, r, scale):
		pt1 = Point(int(r.x*scale), int(r.y*scale))
		pt2 = Point(int((r.x+r.width)*scale), int((r.y+r.height)*scale))
		super(Feature, self).__init__(pt1, pt2)
	
	def __repr__(self):
		return "Feature(%s, %s)" % (self.upper_left, self.lower_right) 