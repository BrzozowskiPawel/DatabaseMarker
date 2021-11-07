import cv2

# This functions is responsible for showing every <number> photo.
# Please press any key to show next photo.
def show_photo(list_of_paths, photos_skipped = 5):
    number_of_shown_photo = 1
    photos_to_be_shown = int(len(list_of_paths) / photos_skipped) + 1
    number_of_photo = 1
    file_index = 0

    for file_path  in list_of_paths:
        if file_index == 0:
            img = cv2.imread(file_path)
            window_title = set_window_title(file_path=file_path, number_of_shown_photo=number_of_shown_photo, photos_to_be_shown=photos_to_be_shown)
            cv2.imshow(window_title, img)
            cv2.waitKey(0)  # waits until a key is pressed
            cv2.destroyAllWindows()  # destroys the window showing image
            number_of_shown_photo = number_of_shown_photo + 1

        number_of_photo = number_of_photo + 1
        file_index = file_index + 1

        if file_index >= photos_skipped:
            file_index = 0


def set_window_title(file_path, number_of_shown_photo, photos_to_be_shown):
    if number_of_shown_photo == photos_to_be_shown:
        return "LAST PHOTO TO MARK: " + file_path + " [" + str(number_of_shown_photo) + "/" + str(
            photos_to_be_shown) + "]"
    else:
        return "Currently marking: " + file_path + " [" + str(number_of_shown_photo) + "/" + str(
            photos_to_be_shown) + "]"

