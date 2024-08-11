import os

parent_folder = "24"

subfolders = range(1, 13)

def create_directory_structure(base_path="."):
    parent_folder_path = os.path.join(base_path, parent_folder)
    os.makedirs(parent_folder_path, exist_ok=True)
    for subfolder in subfolders:
        subfolder_path = os.path.join(parent_folder_path, str(subfolder))
        os.makedirs(subfolder_path, exist_ok=True)

create_directory_structure()
