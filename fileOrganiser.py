import os
import shutil

# Define directories(Replace Username if on Mac)
download_dir = '/Users/Username/Downloads'
music_dir = '/Users/Username/Downloads/Music' 
video_dir = '/Users/Username/Videos'
zip_dir = '/Users/Username/Downloads/Zips'
img_dir = '/Users/Username/Downloads/Images'
doc_dir = '/Users/Username/Downloads/Docs'

# Directory for miscellaneous files
misc_dir = '/Users/Username/Downloads/Miscellaneous'

# Define file extensions
music_arr = ["mp3", "wav"]
img_arr = ["jpg", "png", "jpeg", "webp", "heic",
           "gif", "svg"]
zip_arr = ["zip"]
vid_arr = ["mov", "mp4"]
doc_arr = ["txt", "docx", "pdf", "xlsx", "xlsm"]

# Function to move files


def move_func(root_file, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    shutil.move(root_file, target_folder)
    print(f"Moved: {root_file} to {target_folder}")

# Function to check and move files based on their extensions


def ext_check(ext_in, filepath):
    ext_in = ext_in.lower()
    if ext_in in music_arr:
        move_func(filepath, music_dir)
    elif ext_in in img_arr:
        move_func(filepath, img_dir)
    elif ext_in in zip_arr:
        move_func(filepath, zip_dir)
    elif ext_in in vid_arr:
        move_func(filepath, video_dir)
    elif ext_in in doc_arr:
        move_func(filepath, doc_dir)
    else:
        move_func(filepath, misc_dir)
        print(
            f"Extension '{ext_in}' not recognized for file: {filepath}, moved to Miscellaneous")


# Main script to iterate over files in the download directory
for filename in os.listdir(download_dir):
    filepath = os.path.join(download_dir, filename)
    if os.path.isfile(filepath):
        ext = filename.split('.')[-1]
        ext_check(ext, filepath)
    else:
        print(f"Skipping non-file: {filepath}")
