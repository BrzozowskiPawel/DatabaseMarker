import cv2


class BoundingBox:
    def __init__(self, path,x_,y_,x,y):
        self.path = path
        self.x_ = x_
        self.y_ = y_
        self.x = x
        self.y = y

