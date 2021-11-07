import cv2


class BoundingBox:
    def __init__(self, name,x,y,dx,dy):
        self.name = name
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

