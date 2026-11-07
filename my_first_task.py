import os
import shutil

# 1) YANGI: lug'at
CATEGORIES = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents",
    ".zip": "Archives",
}

path = input("Enter path: ")
files = os.listdir(path)
for file in files:
    filename, extension = os.path.splitext(file)

    # 2) O'ZGARDI: [1:] o'rniga lower() va kategoriya aniqlash
    extension = extension.lower()
    if extension in CATEGORIES:
        folder_name = CATEGORIES[extension]
    else:
        folder_name = "Other"

    # 3) O'ZGARDI: extension o'rniga folder_name
    if os.path.exists(path+'/'+folder_name):
        shutil.move(path+'/'+file, path+'/'+folder_name+'/'+file)
    else:
        os.makedirs(path+'/'+folder_name)
        shutil.move(path+'/'+file, path+'/'+folder_name+'/'+file)