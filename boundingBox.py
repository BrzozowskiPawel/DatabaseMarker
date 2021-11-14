import cv2


class BoundingBox:
    def __init__(self, path,x_,y_,x,y):
        self.path = path
        self.x_ = x_
        self.y_ = y_
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x_, self.y_

    def get_width_height(self):
        w = abs(self.x_ - self.x)
        h = abs(self.y_ - self.y)
        return w,h
