import os

# Function responsible for obtaining a list of photos, that have been placed to mark (Please use .jpg).

# TODO (not important now) - make this go for only directories that haven't been used.
# Thanks to this, you can send new files to the input directory without deleting the previously used ones.

def get_path_for_files(path = "input/", print_files_name = False):
    # Get all the files (their names) in the input folder
    filenames = next(os.walk(path), (None, None, []))[2]  # [] if no file
    tmp_list = []
    # Filtering whether a given file is in .mp4 format and also,
    # whether the folder for a given name has not been previously created.
    # When both conditions are true the filename (which actually is its path)
    # are added to the list which will be returned last.
    for file in filenames:
        if '.jpg' in file:
            folder_path_exist_check = file.replace(".jpg", "")
            tmp_list.append('input/' + file)
    print(f"Founded {len(tmp_list)} files in {path}")
    if print_files_name:
        print(tmp_list)
    return tmp_list
