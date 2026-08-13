import os
import shutil

source_dir = "downloads"
target_dir = "organized_files"

os.makedirs(target_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    source_path = os.path.join(source_dir, filename)
    
    if os.path.isfile(source_path):
        file_ext = filename.split(".")[-1].lower() if "." in filename else "no_extension"
        ext_folder = os.path.join(target_dir, file_ext)
        
        os.makedirs(ext_folder, exist_ok=True)
        shutil.move(source_path, os.path.join(ext_folder, filename))