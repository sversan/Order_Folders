import os
import shutil
from pathlib import Path
from colorama import Fore
# Specify the directory you want to organize
directory = "/home/phoenix/Downloads"  # Change this to your target directory

# Create a dictionary to map file extensions to folder names
file_type_mapping = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",
    ".zip": "Archives",
    ".rar": "Archives",
    ".tar.gz": "Archives",
    ".7z": "Archives",
    ".py": "Scripts",
    ".sh": "Scripts",
    ".cpp": "Code",
    ".java": "Code",
    ".html": "Web",
    ".css": "Web",
    ".js": "Web",
}

def organize_files_by_type(directory):
    # Ensure the target directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Iterate over all files in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # Skip directories
        if os.path.isdir(item_path):
            continue

        # Get file extension
        file_extension = Path(item).suffix.lower()

        # Determine the target folder based on file extension
        target_folder = file_type_mapping.get(file_extension, "Others")

        # Create the target folder if it doesn't exist
        target_folder_path = os.path.join(directory, target_folder)
        os.makedirs(target_folder_path, exist_ok=True)

        # Move the file to the target folder
        try:
            shutil.move(item_path, target_folder_path)
            print(Fore.CYAN,f"Moved '{item}' to '{target_folder}'")
        except Exception as e:
            print(f"Error moving '{item}': {e}")

if __name__ == "__main__":
    organize_files_by_type(directory)
