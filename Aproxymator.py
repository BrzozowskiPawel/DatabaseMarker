from boundingBox import BoundingBox


class Aproxymator:
    def __init__(self, bounding_boxes):
        self.bounding_boxes = bounding_boxes
        self.GLOBAL_BoundingBox_Index = 1
        self.path_first_part = self.prepare_path()


    def prepare_path(self):
        spited_path = self.bounding_boxes[0].path.split("/")
        result = spited_path[1][0:6]
        return result

    # MAIN FUNCTIONALITY BELOW:
    # This functions returns the list of checkboxes
    # WITHOUT FIRST AND LAST ONE (IT SHOULD BE ALREADY MARKED)!
    def get_bounding_box_approximation(self, skipped_number):
        new_bounding_box_list = []
        path_index = 0
        for index in range(0, len(self.bounding_boxes) - 1):
            new_bounding_box_list.append(self.bounding_boxes[index])
            path_index =+ 1
            for _ in range((skipped_number - 2)):
                path_index =+ 1
                newX, newY = self.get_new_x_y(skipped_number, index, index + 1)
                newW, newH = self.get_new_w_h(skipped_number, index, index + 1)
                tmpBB = BoundingBox(path="output/" + self.path_first_part + str(path_index) + ".jpg", x=newX, y=newY, w=newW, h=newH)
                new_bounding_box_list.append(tmpBB)
                self.GLOBAL_BoundingBox_Index += 1
        return new_bounding_box_list

    def get_new_x_y(self, skipped_number, firs_index, second_index):
        x1, y1 = self.bounding_boxes[firs_index].get_coordinates
        x2, y2 = self.bounding_boxes[second_index].get_coordinates
        newX1 = 0
        newY1 = 0
        if (x2 > x1) and (y2 > y1):
            # RIGHT UPPER CORNER
            delta_x = int((x2 - x1) / (skipped_number - 2))
            delta_y = int((y2 - y1) / (skipped_number - 2))
            newX1 = x1 + (delta_x * self.GLOBAL_BoundingBox_Index)
            newY1 = y1 + (delta_y * self.GLOBAL_BoundingBox_Index)
        elif (x2 > x1) and (y2 < y1):
            # RIGHT BOTTOM CORNER
            delta_x = int((x2 - x1) / (skipped_number - 2))
            delta_y = int((y1 - y2) / (skipped_number - 2))
            newX1 = x1 + (delta_x * self.GLOBAL_BoundingBox_Index)
            newY1 = y1 - (delta_y * self.GLOBAL_BoundingBox_Index)
        elif (x2 < x1) and (y2 < y1):
            # LEFT BOTTOM CORNER
            delta_x = int((x1 - x2) / (skipped_number - 2))
            delta_y = int((y1 - y2) / (skipped_number - 2))
            newX1 = x1 - (delta_x * self.GLOBAL_BoundingBox_Index)
            newY1 = y1 - (delta_y * self.GLOBAL_BoundingBox_Index)
        elif (x2 < x1) and (y2 > y1):
            # LEFT UPPER CORNER
            delta_x = int((x1 - x2) / (skipped_number - 2))
            delta_y = int((y2 - y1) / (skipped_number - 2))
            newX1 = x1 - (delta_x * self.GLOBAL_BoundingBox_Index)
            newY1 = y1 + (delta_y * self.GLOBAL_BoundingBox_Index)
        return int(newX1), int(newY1)

    # THIS FUNCTION IS RESPONSIBLE FOR CALCULATING WITH AND HEIGHT FOR NEXT BB.
    def get_new_w_h(self, skipped_number, firs_index, second_index):
        w1, h1 = self.bounding_boxes[firs_index].get_width_height
        w2, h2 = self.bounding_boxes[second_index].get_width_height
        if (w1 > w2) and (h1 > h2):
            # WIDTH is decreasing, HEIGHT is decreasing
            delta_w = (w1 - w2) / (skipped_number - 1)
            delta_h = (h1 - h2) / (skipped_number - 1)
            newW1 = w1 + (delta_w * self.GLOBAL_BoundingBox_Index)
            newH1 = h1 + (delta_h * self.GLOBAL_BoundingBox_Index)
        elif (w1 > w2) and (h1 < h2):
            # WIDTH is decreasing, HEIGHT is increasing
            delta_w = (w1 - w2) / (skipped_number - 1)
            delta_h = (h2 - h1) / (skipped_number - 1)
            newW1 = w1 + (delta_w * self.GLOBAL_BoundingBox_Index)
            newH1 = h1 - (delta_h * self.GLOBAL_BoundingBox_Index)
        elif (w1 < w2) and (h1 < h2):
            # WIDTH is increasing, HEIGHT is increasing
            delta_w = (w2 - w1) / (skipped_number - 1)
            delta_h = (h2 - h1) / (skipped_number - 1)
            newW1 = w1 - (delta_w * self.GLOBAL_BoundingBox_Index)
            newH1 = h1 - (delta_h * self.GLOBAL_BoundingBox_Index)
        elif (w1 < w2) and (h1 > h2):
            # WIDTH is increasing, HEIGHT is decreasing
            delta_w = (w2 - w1) / (skipped_number - 1)
            delta_h = (h1 - h2) / (skipped_number - 1)
            newW1 = w1 - (delta_w * self.GLOBAL_BoundingBox_Index)
            newH1 = h1 + (delta_h * self.GLOBAL_BoundingBox_Index)
        return int(newW1), int(newH1)

    # def set_skipped_number(self, skipped_number):
    #     self.skipped_number = skipped_number

