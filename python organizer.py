import os
import shutil

# Folder path
path = input("Enter folder path: ")

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],   
    "Python Files": [".py"]
}

# Check if folder exists
if not os.path.exists(path):
    print("Invalid folder path!")
    exit()

# Organize files
for file in os.listdir(path):

    file_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    moved = False

    # Get extension
    _, extension = os.path.splitext(file)

    # Match extension
    for folder_name, extensions in file_types.items():

        if extension.lower() in extensions:

            folder_path = os.path.join(path, folder_name)

            # Create folder if not exists
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            # Move file
            shutil.move(file_path, os.path.join(folder_path, file))

            print(f"Moved: {file} → {folder_name}")

            moved = True
            break

    # Uncategorized files
    if not moved:

        other_folder = os.path.join(path, "Others")

        if not os.path.exists(other_folder):
            os.mkdir(other_folder)

        shutil.move(file_path, os.path.join(other_folder, file))

        print(f"Moved: {file} → Others")

print("\nFiles organized successfully!")