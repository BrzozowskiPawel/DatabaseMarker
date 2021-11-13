import cv2
from dataclasses import dataclass
from boundingBox import BoundingBox

bounding_box_list = []
x_, y_ = None, None
isDrawing = False
img, canvas = None, None
current_file_path = None
selections = []


@dataclass
class Selection:
    x: float
    y: float
    x_: float
    y_: float


def showSelections():
    for selection in selections:
        cv2.rectangle(canvas, (selection.x_, selection.y_), (selection.x, selection.y), (255, 0, 0), 2)
    cv2.imshow(current_file_path, canvas)


# This functions is responsible for showing every <number> photo.
# Please press any key to show next photo.
def show_photo(list_of_paths, photos_skipped=5):
    file_index = 0
    global canvas, current_file_path
    for file_path in list_of_paths:
        if file_index == 0:
            current_file_path = file_path
            img = cv2.imread(current_file_path)
            canvas = img.copy()
            cv2.namedWindow(current_file_path)
            cv2.setMouseCallback(current_file_path, click_event)
            while (True):
                cv2.imshow(current_file_path, canvas)
                k = cv2.waitKey(0)
                if k == 27:
                    selections.clear()
                    break
                elif k == ord('d'):
                    element_to_remove = len(selections) - 1
                    del selections[element_to_remove]
                    canvas = img.copy()
                    showSelections()
            cv2.destroyAllWindows()
        file_index = file_index + 1
        if file_index >= photos_skipped:
            file_index = 0


def click_event(event, x, y, flags, param):
    global x_, y_, isDrawing, current_file_path, canvas
    if event == cv2.EVENT_LBUTTONDOWN:
        x_, y_ = x, y
        # print(x_, ' ', y_)
        isDrawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDrawing:
            imgCopy = canvas.copy()
            cv2.rectangle(imgCopy, (x_, y_), (x, y), (255, 0, 0), 2)
            cv2.imshow(current_file_path, imgCopy)
    elif event == cv2.EVENT_LBUTTONUP:
        selection = Selection(x_, y_, x, y)
        selections.append(selection)
        showSelections()
        isDrawing = False
        print(len(selections))


def get_bounding_box_list():
    return bounding_box_list
