import boundingBox

# IMPORTANT GLOBAL VAR
GLOBAL_BoundingBox_Index = 1

# to be set NOT as part of this file 0 should be already declared
skipped_number = 0 # Have to be set in def show_photo()

# Doesnt have to be global (arent modified by functions just for read):
x1, x2, y1, y2 = 0  # x1,y1 -> cords for first human made rectangle
                    # x2,y2 -> cords for second human made rectangle.
                    # This could be for ex. 10 photos apart, I am only considering photos
                    # that have been manually marked.

w1,h1, w2, h2 = 0   # The same rule like before but for width and height.

# TODO; CRITICAL!
# THIS NEEDS TO BE USED ONLY ON SECOND PHOTO FROM DRAWING RECTANGLE.
# AFTER THAT FUNCTION BELLOW SHOULD BE USED!



# MAIN FUNCTIONALITY BELOW:
# This functions returns the list of checkboxes
# WITHOUT FIRST AND LAST ONE (IT SHOULD BE ALREADY MARKED)!
def get_boundingBox_approximation():
    global GLOBAL_BoundingBox_Index
    BoundingBoxList = []
    for _ in range((skipped_number - 2)):
        newX, newY = get_new_x_y()
        newW, newH = get_new_w_h()
        tmpBB = boundingBox.BoundingBox(name="NIL", x=newX, y=newY, w=newW, h=newH)
        BoundingBoxList.append(tmpBB)
        GLOBAL_BoundingBox_Index += 1

    GLOBAL_BoundingBox_Index = 0
    return BoundingBoxList


# ------------------------------------------------------------------------------------------
# FUNCTIONS BELOW ARE EXTRA FUNCTIONS USED ONLY INSIDE OF
# ------------------------------------------------------------------------------------------


# THIS FUNCTION IS RESPONSIBLE FOR CALCULATING NEW X,Y CORD FOR NEW BB
def get_new_x_y():
    newX1 = 0
    newY1 = 0
    if (x2 > x1) and (y2 > y1):
        # RIGHT UPPER CORNER
        delta_x = int((x2 - x1) / (skipped_number - 2))
        delta_y = int((y2 - y1) / (skipped_number - 2))
        newX1 = x1 + (delta_x * GLOBAL_BoundingBox_Index)
        newY1 = y1 + (delta_y * GLOBAL_BoundingBox_Index)
    elif (x2 > x1) and (y2 < y1):
        # RIGHT BOTTOM CORNER
        delta_x = int((x2 - x1) / (skipped_number - 2))
        delta_y = int((y1 - y2) / (skipped_number - 2))
        newX1 = x1 + (delta_x * GLOBAL_BoundingBox_Index)
        newY1 = y1 - (delta_y * GLOBAL_BoundingBox_Index)
    elif (x2 < x1) and (y2 < y1):
        # LEFT BOTTOM CORNER
        delta_x = int((x1 - x2) / (skipped_number - 2))
        delta_y = int((y1 - y2) / (skipped_number - 2))
        newX1 = x1 - (delta_x * GLOBAL_BoundingBox_Index)
        newY1 = y1 - (delta_y * GLOBAL_BoundingBox_Index)
    elif (x2 < x1) and (y2 > y1):
        # LEFT UPPER CORNER
        delta_x = int((x1 - x2) / (skipped_number - 2))
        delta_y = int((y2 - y1) / (skipped_number - 2))
        newX1 = x1 - (delta_x * GLOBAL_BoundingBox_Index)
        newY1 = y1 + (delta_y * GLOBAL_BoundingBox_Index)
    return int(newX1), int(newY1)

# THIS FUNCTION IS RESPONSIBLE FOR CALCULATING WITH AND HEIGHT FOR NEXT BB.
def get_new_w_h():
    if (w1 > w2) and (h1 > h2):
        # WIDTH is decreasing, HEIGHT is decreasing
        delta_w = (w1-w2) / (skipped_number - 1)
        delta_h = (h1-h2) / (skipped_number - 1)
        newW1 =  w1 + (delta_w * GLOBAL_BoundingBox_Index)
        newH1 = h1 + (delta_h * GLOBAL_BoundingBox_Index)
    elif (w1 > w2) and (h1 < h2):
        # WIDTH is decreasing, HEIGHT is increasing
        delta_w = (w1 - w2) / (skipped_number - 1)
        delta_h = (h2 - h1) / (skipped_number - 1)
        newW1 = w1 + (delta_w * GLOBAL_BoundingBox_Index)
        newH1 = h1 - (delta_h * GLOBAL_BoundingBox_Index)
    elif (w1 < w2) and (h1 < h2):
        # WIDTH is increasing, HEIGHT is increasing
        delta_w = (w2 - w1) / (skipped_number - 1)
        delta_h = (h2 - h1) / (skipped_number - 1)
        newW1 = w1 - (delta_w * GLOBAL_BoundingBox_Index)
        newH1 = h1 - (delta_h * GLOBAL_BoundingBox_Index)
    elif (w1 < w2) and (h1 > h2):
        # WIDTH is increasing, HEIGHT is decreasing
        delta_w = (w2 - w1) / (skipped_number - 1)
        delta_h = (h1 - h2) / (skipped_number - 1)
        newW1 = w1 - (delta_w * GLOBAL_BoundingBox_Index)
        newH1 = h1 + (delta_h * GLOBAL_BoundingBox_Index)
    return int(newW1),int(newH1)