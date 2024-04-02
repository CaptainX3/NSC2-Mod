"""
Copy all the dds files from all subdirectories in src
to the respective directories in the parent folder

Usage: python deploydds.py
"""

import os
import shutil
# Get the current directory
current_dir = os.getcwd()

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Iterate through all subdirectories in the current directory
for root, dirs, files in os.walk(current_dir):
    for file in files:
        # Check if the file has a .dds extension
        if file.endswith(".dds"):
            # Get the relative path of the file
            relative_path = os.path.relpath(root, current_dir)

            # Create the destination directory path in the parent directory
            destination_dir = os.path.join(parent_dir, relative_path)

            # Create the destination directory if it doesn't exist
            os.makedirs(destination_dir, exist_ok=True)

            # Copy the file to the destination directory when file does not exist or is out of date
            if not os.path.exists(os.path.join(destination_dir, file)) \
                or os.path.getmtime(os.path.join(root, file)) > \
                    os.path.getmtime(os.path.join(destination_dir, file)):
                shutil.copy2(os.path.join(root, file), destination_dir)
