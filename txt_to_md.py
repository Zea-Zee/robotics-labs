import os
import shutil

# Define the root directory
root_dir = '/home/zea/Desktop/robotics-labs/'

# Walk through the directory to find all readme.md files
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename == 'readme.md':
            # Construct the full path of the readme.md file
            old_file = os.path.join(dirpath, filename)
            new_file = os.path.join(dirpath, 'readme.txt')
            # Copy the readme.md file to description.txt
            shutil.copy(old_file, new_file)

print("Files copied successfully!")
