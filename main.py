import path_finder
import show_photos


# Getting path for everything file in particular photos directory.
# This method required path (String type) as parameter in other case it's use default.
path_list = path_finder.get_path_for_files(path="dataTMP/")
print(path_list)

# TODO check what in case that there will be more different folders with photos instead just 1.
# Showing very <photos_skipped> photo.
# Please specify <list_of_paths> as list that you have gotten from get_path_for_files()
anotated_photos = show_photos.show_photo(list_of_paths=path_list, photos_skipped=5)