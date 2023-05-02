import os
import shutil

# define the path to the folder containing the files to be categorized
folder_path = '/path/to/folder'

# create a dictionary to map file extensions to folder names
extension_map = {
    '.jpg': 'images',
    '.png': 'images',
    '.gif': 'images',
    '.pdf': 'documents',
    '.doc': 'documents',
    '.txt': 'documents',
    '.mp3': 'music',
    '.wav': 'music',
    '.flac': 'music',
    '.mp4': 'videos',
    '.avi': 'videos',
    '.mov': 'videos',
}

# loop through the files in the folder
for filename in os.listdir(folder_path):
    # get the file extension
    extension = os.path.splitext(filename)[1].lower()
    # check if the extension is in the mapping dictionary
    if extension in extension_map:
        # if the folder doesn't exist, create it
        folder_name = extension_map[extension]
        folder_path = os.path.join(folder_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # move the file to the appropriate folder
        source_path = os.path.join(folder_path, filename)
        shutil.move(os.path.join(folder_path, filename), source_path)