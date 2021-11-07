import cv2
import numpy as np


drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle.
ix,iy = -1,-1
current_img = ""


# This functions is responsible for showing every <number> photo.
# Please press any key to show next photo.
def show_photo(list_of_paths, photos_skipped = 5):
    anotated_photos = []
    file_index = 0
    for file_path  in list_of_paths:
        if file_index == 0:
            img = cv2.imread(file_path)
            cv2.imshow(file_path, img)
            cv2.waitKey(0)  # waits until a key is pressed
            cv2.destroyAllWindows()  # destroys the window showing image
            anotated_photos.append(file_path)
        print(f"current index number = {file_index} - file: {file_path}")
        file_index = file_index + 1
        if file_index >= photos_skipped:
            file_index = 0
        return anotated_photos

# mouse callback function
def draw_circle(event,x,y,flags,param):
  global ix,iy,drawing,mode

  if event == cv2.EVENT_LBUTTONDOWN:
      drawing = True
      ix,iy = x,y

  elif event == cv2.EVENT_MOUSEMOVE:
    if drawing == True:
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),3)
            a=x
            b=y
            if a != x | b != y:
                 cv2.rectangle(img,(ix,iy),(x,y),(0,0,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

  elif event == cv2.EVENT_LBUTTONUP:
    drawing = False
    if mode == True:
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)

    else:
        cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
 cv2.imshow('image',img)
 k = cv2.waitKey(1) & 0xFF
 if k == ord('m'):
    mode = not mode
 elif k == 27:
    break

cv2.destroyAllWindows()