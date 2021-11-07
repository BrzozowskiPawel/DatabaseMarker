import cv2

x_, y_ = None, None
dx_, dy_ = None, None
first_click = True
img = None
# This functions is responsible for showing every <number> photo.
# Please press any key to show next photo.
def show_photo(list_of_paths, photos_skipped=5):
    file_index = 0
    global img
    for file_path in list_of_paths:
        if file_index == 0:
            img = cv2.imread(file_path)
            cv2.imshow(file_path, img)
            cv2.setMouseCallback(file_path, click_event)
            cv2.waitKey(0)  # waits until a key is pressed
            cv2.destroyAllWindows()  # destroys the window showing image
        # print(f"current index number = {file_index} - file: {file_path}")
        file_index = file_index + 1
        if file_index >= photos_skipped:
            file_index = 0


def click_event(event, x, y, flags, param):
    global x_, y_, dx_, dy_
    global first_click
    if not first_click:
        if event == cv2.EVENT_LBUTTONUP:
            dx_, dy_ = x, y
            print(dx_, ' x ', dy_)
            first_click = True
            cv2.rectangle(img, (x_,y_), (dx_,dy_), (255, 0, 0), 2)
            cv2.imshow("result", img)
            return
    if first_click:
        if event == cv2.EVENT_LBUTTONDOWN:
            x_, y_ = x, y
            print(x_, ' ', y_)
            first_click = False
            return



