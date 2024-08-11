import os

top_level_folders = ["24", "25", "26"]

subfolders = range(1, 13)

def create_directory_structure(base_path="."):
    for top_folder in top_level_folders:
        top_folder_path = os.path.join(base_path, top_folder)
        os.makedirs(top_folder_path, exist_ok=True)
        for subfolder in subfolders:
            subfolder_path = os.path.join(top_folder_path, str(subfolder))
            os.makedirs(subfolder_path, exist_ok=True)


create_directory_structure()
