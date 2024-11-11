import os

# Define the root directory
root_dir = '/home/zea/Desktop/robotics-labs/'

# Walk through the directory to find all description.txt files
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename == 'description.txt':
            # Construct the full path of the file
            old_file = os.path.join(dirpath, filename)
            new_file = os.path.join(dirpath, 'readme.md')
            # Rename the file
            os.rename(old_file, new_file)

"Files renamed successfully!"
