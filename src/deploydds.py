"""
Copy all the dds files from all subdirectories in src
to the respective directories in the parent folder

Usage: python deploydds.py
"""

import os
import shutil
# ANSI shell tags for color
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
NC = "\033[0m"

# Set current working directory as the directory of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Use as the current directory
current_dir = os.getcwd()
print(f"Deploying DDS...\nCurrent directory: {YELLOW}{current_dir}{NC}")
# Get the parent directory
parent_dir = os.path.dirname(current_dir)
print(f"Parent directory: {YELLOW}{parent_dir}{NC}")

# Iterate through all subdirectories in the current directory
for root, dirs, files in os.walk(current_dir):
    for file in files:
        # Check if the file has a .dds extension
        if file.endswith(".dds"):
            # print(f"Found DDS file: {file} in {root}")
            # Get the relative path of the file
            relative_path = os.path.relpath(root, current_dir)

            # Create the destination directory path in the parent directory
            destination_dir = os.path.join(parent_dir, relative_path)

            # Create the destination directory if it doesn't exist
            os.makedirs(destination_dir, exist_ok=True)

            # Copy over the new file
            print(f"Copying {GREEN}{file}{NC} to {YELLOW}{destination_dir}{NC}")
            shutil.copy2(os.path.join(root, file), destination_dir)
