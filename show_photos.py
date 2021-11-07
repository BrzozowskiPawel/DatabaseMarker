import cv2

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